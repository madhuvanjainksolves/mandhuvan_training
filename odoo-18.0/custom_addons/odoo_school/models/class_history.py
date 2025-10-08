from odoo import models, fields

class StudentClassHistory(models.Model):
    _name = 'school.class.history'
    _description = 'Student Class History'

    student_id = fields.Many2one('school.student', string='Student', required=True, ondelete='cascade')
    old_class_id = fields.Many2one('school.class', string='Previous Class')
    new_class_id = fields.Many2one('school.class', string='New Class')
    changed_date = fields.Datetime(string='Date Changed', default=fields.Datetime.now)
    result_file = fields.Binary("Result File")
    result_filename = fields.Char("Filename")
