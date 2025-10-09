from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "Class"

    name = fields.Char(string="Class Name", required=True)
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    student_ids = fields.One2many('school.student', 'class_id', string="Students")
    fee_structure_ids = fields.One2many('school.fee.structure', 'class_id', string="Fee Structures")
