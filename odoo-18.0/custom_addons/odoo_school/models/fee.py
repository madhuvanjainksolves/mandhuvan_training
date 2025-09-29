from odoo import models, fields

class Fees(models.Model):
    _name = "school.fee"
    _description = "Fee"

    name = fields.Char(string="Description")
    student_id = fields.Many2one("school.student", string="Student")
    month = fields.Selection([
        ('1', 'First Class'), ('2', 'Second Class'), ('3', 'Third Class'),
        ('4', 'Fourth Class'), ('5', 'Fifth Class'), ('6', 'Sixth Class'),
        ('7', 'Seventh Class'), ('8', 'Eights Class'), ('9', 'Ninth Class'),
        ('10', 'Tenth Class'), ('11', 'Eleventh Class'), ('12', 'C Class')
    ], string="Class Fee")
    amount = fields.Float(string="Amount")
