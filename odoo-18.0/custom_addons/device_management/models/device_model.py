from odoo import api, fields, models

class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'


    name = fields.Char(required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")
    device_ids = fields.One2many('device.device', 'device_model_id', string="Devices")