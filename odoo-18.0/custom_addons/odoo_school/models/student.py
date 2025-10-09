from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(required=True)
    age = fields.Integer()
    class_id = fields.Many2one('school.class', string="Current Class")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    marksentry_ids = fields.One2many('school.student.marks', 'student_id', string="Marks")
    fee_ids = fields.One2many('school.fee', 'student_id', string="Fees")
    class_history_ids = fields.One2many('school.class.history', 'student_id', string="Class History")
    previous_marks_ids = fields.One2many('school.student.marks', compute='_compute_previous_marks', string="Previous Results")
    # result_file = fields.Binary("Report File")
    # result_filename = fields.Char("Filename")
    has_previous_marks = fields.Boolean(string='Has Previous Marks', compute='_compute_has_previous_marks', store=False)

    @api.onchange('class_id')
    def _onchange_class_id(self):

        if self.class_id:
            self.subject_ids = [(6, 0, self.class_id.subject_ids.ids)]

        if self._origin and self._origin.class_id and self._origin.class_id != self.class_id:
            self.env['school.class.history'].create({
                'student_id': self.id,
                'old_class_id': self._origin.class_id.id,
                'new_class_id': self.class_id.id,
            })

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('class_id'):
                class_record = self.env['school.class'].browse(vals['class_id'])
                if class_record and class_record.subject_ids:
                    vals['subject_ids'] = [(6, 0, class_record.subject_ids.ids)]
        return super().create(vals_list)

    def write(self, vals):
        if 'class_id' in vals:
            for rec in self:
                old_class = rec.class_id
                new_class = self.env['school.class'].browse(vals.get('class_id'))
                if old_class and old_class != new_class:
                    self.env['school.class.history'].create({
                        'student_id': rec.id,
                        'old_class_id': old_class.id,
                        'new_class_id': new_class.id,
                    })

            new_class = self.env['school.class'].browse(vals.get('class_id'))
            if new_class and new_class.subject_ids:
                vals['subject_ids'] = [(6, 0, new_class.subject_ids.ids)]

        return super().write(vals)

    def _compute_previous_marks(self):
        for student in self:
            prev = self.env['school.student.marks'].search([
                ('student_id', '=', student.id),
                ('marks_entry_id.class_id', '!=', student.class_id.id if student.class_id else False),
            ])
            student.previous_marks_ids = prev

    @api.depends('previous_marks_ids')
    def _compute_has_previous_marks(self):
        for record in self:
            record.has_previous_marks = bool(record.previous_marks_ids)
