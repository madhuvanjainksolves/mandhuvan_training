from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    class_id = fields.Many2one('school.class', string="Current Class")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    marksentry_ids = fields.One2many('school.student.marks', 'student_id', string="Marks")
    fee_ids = fields.One2many('school.fee', 'student_id', string='Fees')
    class_history_ids = fields.One2many('school.class.history', 'student_id', string="Class History")
    previous_history_ids = fields.One2many('school.class.history', 'student_id', string="Previous History", compute="_compute_previous_history")


    count_history = fields.Integer(string="Previous Record", compute='_compute_count_history')

    def _compute_count_history(self):
        for rec in self:
            rec.count_history = len(rec.class_history_ids)

    def open_class_history(self):
        return {
            'name': _('Class History'),
            'domain': [('student_id', '=', self.id)],
            'res_model': 'school.class.history',
            'view_mode': 'list,form',
            'type': 'ir.actions.act_window',
        }

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('class_id'):
                cls = self.env['school.class'].browse(vals['class_id'])
                if cls and cls.subject_ids:
                    vals['subject_ids'] = [(6, 0, cls.subject_ids.ids)]
        students = super().create(vals_list)
        for stud in students:
            if stud.class_id:
                stud.env['school.class.history'].create({
                    'student_id': stud.id,
                    'old_class_id': False,
                    'new_class_id': stud.class_id.id,
                })
        return students

    def write(self, vals):
        if 'class_id' in vals:
            for rec in self:
                old_cls = rec.class_id
                new_cls = self.env['school.class'].browse(vals['class_id'])
                if old_cls and new_cls and old_cls.id != new_cls.id:
                    # create a history record
                    self.env['school.class.history'].create({
                        'student_id': rec.id,
                        'old_class_id': old_cls.id,
                        'new_class_id': new_cls.id,
                    })
            new_cls = self.env['school.class'].browse(vals['class_id'])
            if new_cls and new_cls.subject_ids:
                vals['subject_ids'] = [(6, 0, new_cls.subject_ids.ids)]
        return super().write(vals)
