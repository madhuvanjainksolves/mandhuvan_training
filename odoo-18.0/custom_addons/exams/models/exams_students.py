from odoo import api, fields, models

class ExamStudent(models.Model):
    _name = "exams.students"
    _description = "Students"

    name = fields.Char(string="Name", required=True)
    class_id = fields.Char(string="Class")
    roll_number = fields.Char(string="Roll Number")
    exam_ids = fields.One2many('exams.exam', 'student_id', string="Exams")
