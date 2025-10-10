from odoo import models, fields

class FeeStructure(models.Model):
    _name = 'school.fee.structure'
    _description = 'Fee Structure for a Class'

    class_id = fields.Many2one('school.class', string="Class", required=True, ondelete='cascade')
    name = fields.Char(string="Name / Term")
    amount = fields.Float(string="Fee Amount", required=True)
    active = fields.Boolean(default=True)

