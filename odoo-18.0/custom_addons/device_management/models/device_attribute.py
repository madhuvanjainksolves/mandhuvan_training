from odoo import api, fields, models

class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'


    name = fields.Char(required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    required = fields.Boolean(default=False)
    device_attribute_value_ids = fields.One2many('device.attribute.value', 'device_attribute_id', string="Values")