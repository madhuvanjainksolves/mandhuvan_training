from odoo import api, fields, models

class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'


    name = fields.Char(required=True, unique=True)
    code = fields.Char(required=True, unique=True)
    sequence = fields.Integer()
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Models")
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Attributes")
    device_ids = fields.One2many('device.device', 'device_type_id', string="Devices")