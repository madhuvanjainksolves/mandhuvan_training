from odoo import api, fields, models

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'
    _sql_constraints = [
    ('unique_device_attribute', 'unique(device_id, device_attribute_id)',
    'Each attribute can only be assigned once per device!')
    ]


    device_id = fields.Many2one('device.device', string="Device", required=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Attribute", required=True)
    device_attribute_value_id = fields.Many2one('device.attribute.value', string="Value")