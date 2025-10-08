# odoo_school/models/subject.py
from odoo import models, fields

class Subject(models.Model):
    _name = "school.subject"
    _description = "Subject"

    name = fields.Char(string="Subject Name", required=True)
    student_ids = fields.Many2many("school.student", string="Students", compute="_compute_students", store=False)

    def _compute_students(self):
        for s in self:
            s.student_ids = self.env['school.student'].search([('subject_ids', 'in', s.id)])
