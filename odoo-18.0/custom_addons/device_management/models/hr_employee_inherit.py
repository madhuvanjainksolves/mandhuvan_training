from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    device_assignment_ids = fields.One2many("device.assignment", "employee_id", string="Device Assignments")
