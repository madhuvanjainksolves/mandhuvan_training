from odoo import models, fields

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "Class"

    name = fields.Char(string="Class Name", required=True)
    student_ids = fields.One2many("school.student", "class_id", string="Students")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
