from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string="Is a Teacher", default=False)
    subject_specialization = fields.Char(string="Subject Specialization")
    class_ids = fields.One2many('school.class', 'teacher_id', string="Classes")
