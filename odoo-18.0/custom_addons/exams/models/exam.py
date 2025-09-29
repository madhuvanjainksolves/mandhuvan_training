from odoo import api, fields, models

class Exam(models.Model):
    _name = "exams.exam"
    _description = "Exam Marks"

    name = fields.Char(string="Exam Name")
    student_id = fields.Many2one('exams.students', string="Student", required=True)
    subject_id = fields.Many2one('exams.subjects', string="Subject", required=True)
    marks = fields.Integer(string="Marks", required=True)
    exam_date = fields.Date(string="Exam Date")
