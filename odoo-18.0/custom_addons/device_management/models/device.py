from odoo import api, fields, models

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'


    name = fields.Char(string="Serial / Name", required=True, unique=True)
    shared = fields.Boolean(default=False)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")
    device_model_id = fields.Many2one('device.model', string="Device Model")
    device_attribute_id = fields.One2many('device.attribute.assignment', 'device_id', string="Attributes")