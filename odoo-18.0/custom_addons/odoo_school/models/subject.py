from odoo import models, fields

class Subject(models.Model):
    _name = "school.subject"
    _description = "Subject"

    name = fields.Char(string="Subject Name", required=True)
    # Many2many
    student_ids = fields.Many2many("school.student", string="Students")

