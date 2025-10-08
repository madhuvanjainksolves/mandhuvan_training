from odoo import api, fields, models

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'

    name = fields.Char(string="Name", required=True)
    shared = fields.Boolean(default=False)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_model_id = fields.Many2one('device.model', string="Device Model")
    device_brand_id = fields.Many2one(
        'device.brand',
        related='device_model_id.device_brand_id',
        store=True,
        readonly=True
    )
    device_attribute_id = fields.One2many('device.attribute.assignment', 'device_id', string="Attributes")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The device name must be unique!')
    ]

    @api.onchange('device_type_id')
    def _onchange_device_type_id(self):
        if self.device_type_id:
            model = self.env['device.model'].search(
                [('device_type_id', '=', self.device_type_id.id)], limit=1
            )
            self.device_model_id = model.id if model else False

            self.device_attribute_id = [(5, 0, 0)]
            for attr in self.device_type_id.device_attribute_ids:
                self.device_attribute_id = [(0, 0, {'attribute_id': attr.id})]

            return {
                'domain': {
                    'device_model_id': [('device_type_id', '=', self.device_type_id.id)],
                }
            }
        else:
            self.device_model_id = False
            self.device_attribute_id = [(5, 0, 0)]
            return {
                'domain': {
                    'device_model_id': [],
                }
            }
