from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string="Class Name", required=True)
    teacher_id = fields.Many2one('hr.employee', string="Teacher", domain=[('is_teacher', '=', True)])
