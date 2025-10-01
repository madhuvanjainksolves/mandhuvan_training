from odoo import models, fields

class StudentMarks(models.Model):
    _name = "school.student.marks"
    _description = "Student Marks"

    marks_entry_id = fields.Many2one("school.marks.entry", string="Marks Entry", required=True)
    student_id = fields.Many2one("school.student", string="Student", required=True)
    marks = fields.Integer(string="Marks")
    subject_id = fields.Many2one("school.subject", string="Subject", required=True)

