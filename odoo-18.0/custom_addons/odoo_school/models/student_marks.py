from odoo import api, fields, models

class StudentMarks(models.Model):
    _name = 'school.student.marks'
    _description = 'Marks of Student'

    marks_entry_id = fields.Many2one('school.marks.entry', string="Marks Entry", required=True, ondelete='cascade')
    student_id = fields.Many2one('school.student', string="Student", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    marks = fields.Float(string="Marks")

    previous_marks = fields.Float(string="Previous Class Marks", compute='_compute_previous_marks')

    @api.depends('student_id', 'subject_id')
    def _compute_previous_marks(self):
        for rec in self:
            previous_mark = self.search([
                ('student_id', '=', rec.student_id.id),
                ('subject_id', '=', rec.subject_id.id),
                ('id', '!=', rec.id),
            ], order='id desc', limit=1)
            rec.previous_marks = previous_mark.marks if previous_mark else 0