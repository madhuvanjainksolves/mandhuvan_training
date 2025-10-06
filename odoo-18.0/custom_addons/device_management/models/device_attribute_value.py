from odoo import api, fields, models

class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(required=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Attribute")

    _sql_constraints = [
        ('unique_attribute_value', 'unique(name)', 'Attribute Value name must be unique!'),
        ('unique_attribute_value_per_attribute', 'unique(name, device_attribute_id)', 'This attribute value already exists for this attribute!')
    ]