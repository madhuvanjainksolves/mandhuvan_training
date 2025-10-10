from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MarksEntry(models.Model):
    _name = 'school.marks.entry'
    _description = 'Marks Sheet Entry'

    class_id = fields.Many2one('school.class', string="Class", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True, domain=lambda self: [('id','in',self.class_id.subject_ids.ids)])
    date = fields.Date(string="Date")
    student_marks_ids = fields.One2many('school.student.marks', 'marks_entry_id', string="Marks Lines", copy=False)

    @api.onchange('class_id')
    def _onchange_class_id(self):
        self.subject_id = False

    def action_create_lines(self):
        if not (self.class_id and self.subject_id):
            raise UserError(_("Please select class and subject first."))
        existing = self.env['school.student.marks'].search([
            ('marks_entry_id', '=', self.id)
        ])
        students = self.class_id.student_ids
        for stud in students:
            if not existing.filtered(lambda r: r.student_id.id == stud.id):
                self.env['school.student.marks'].create({
                    'marks_entry_id': self.id,
                    'student_id': stud.id,
                    'subject_id': self.subject_id.id,
                })
        return True
