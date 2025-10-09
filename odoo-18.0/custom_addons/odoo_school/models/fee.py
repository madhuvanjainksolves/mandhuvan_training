from odoo import models, fields

class SchoolFee(models.Model):
    _name = 'school.fee'
    _description = 'Student Fee Record'

    student_id = fields.Many2one('school.student', string="Student", required=True, ondelete='cascade')
    month = fields.Selection([
        ('jan', 'January'), ('feb', 'February'), ('mar', 'March'),
        ('apr', 'April'), ('may', 'May'), ('jun', 'June'),
        ('jul', 'July'), ('aug', 'August'), ('sep', 'September'),
        ('oct', 'October'), ('nov', 'November'), ('dec', 'December')],
        string="Month", required=True)
    amount = fields.Float(string="Amount", required=True)
