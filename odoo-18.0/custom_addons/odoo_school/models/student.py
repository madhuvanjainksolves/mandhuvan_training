from odoo import models, fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    class_id = fields.Many2one("school.class", string="Class")
    subject_ids = fields.Many2many("school.subject", string="Subjects")
    fee_ids = fields.One2many("school.fee", "student_id", string="Fee")

    marksentry_ids = fields.One2many("school.student.marks", "student_id", string="Marks Entries")
