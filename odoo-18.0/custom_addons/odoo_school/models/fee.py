from odoo import models, fields, api

class StudentFee(models.Model):
    _name = 'school.fee'
    _description = 'Fee record for student'

    student_id = fields.Many2one('school.student', string="Student", required=True, ondelete='cascade')
    class_id = fields.Many2one('school.class', string="Class", compute='_compute_class_id', store=True)
    fee_struct_id = fields.Many2one('school.fee.structure', string="Fee Structure", compute='_compute_fee_structure', store=True, readonly=False)
    amount = fields.Float(string="Amount", related='fee_struct_id.amount', readonly=True)
    paid = fields.Boolean(string="Paid?", default=False)
    paid_date = fields.Date(string="Paid Date")
    state = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid')
    ], string="State", compute='_compute_state', store=True)

    @api.depends('student_id')
    def _compute_class_id(self):
        for rec in self:
            rec.class_id = rec.student_id.class_id

    @api.depends('class_id')
    def _compute_fee_structure(self):
        for rec in self:
            if rec.class_id:
                fee_struct = self.env['school.fee.structure'].search([
                    ('class_id', '=', rec.class_id.id),
                    ('active', '=', True)
                ], limit=1)
                rec.fee_struct_id = fee_struct
            else:
                rec.fee_struct_id = False

    @api.depends('paid')
    def _compute_state(self):
        for rec in self:
            rec.state = 'paid' if rec.paid else 'pending'
