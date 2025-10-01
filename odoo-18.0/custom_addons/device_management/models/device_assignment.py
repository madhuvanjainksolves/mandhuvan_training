from odoo import models, fields, api

class DeviceAssignment(models.Model):
    _name = "device.assignment"
    _description = "Device Assignment"

    name = fields.Char(string="Assignment Code", required=True, copy=False, index=True)
    device_id = fields.Many2one("device.device", string="Device", required=True)
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_expire = fields.Date(string="Expire Date")
    state = fields.Selection([
        ("new", "New"),
        ("draft", "Draft"),
        ("approved", "Approved"),
        ("returned", "Returned"),
        ("rejected", "Rejected"),
    ], string="Status", default="new", required=True)

    _sql_constraints = [
        ("unique_assignment", "unique(device_id, employee_id)", "This device is already assigned to the employee!")
    ]
