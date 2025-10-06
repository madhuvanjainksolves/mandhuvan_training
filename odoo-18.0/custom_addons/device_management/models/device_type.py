from odoo import api, fields, models
from odoo.exceptions import ValidationError

class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'
    _order = 'sequence asc, name asc'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    sequence = fields.Integer(string="Sequence", copy=False)
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Attributes")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Models")
    device_ids = fields.One2many('device.device', 'device_type_id', string="Devices")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Error: The device type name must be unique!'),
        ('code_unique', 'unique(code)', 'Error: The device type code must be unique!'),
        ('sequence_unique', 'unique(sequence)', 'Error: The sequence number must be unique!')
    ]

    @api.model
    def default_get(self, fields_list):
        defaults = super(DeviceType, self).default_get(fields_list)
        last_record = self.env['device.type'].search([], order='sequence desc', limit=1)
        defaults['sequence'] = last_record.sequence + 1 if last_record else 1
        return defaults

    @api.constrains('sequence')
    def _check_sequence_unique(self):
        for record in self:
            if self.search_count([('sequence', '=', record.sequence), ('id', '!=', record.id)]):
                raise ValidationError("Sequence must be unique!")
