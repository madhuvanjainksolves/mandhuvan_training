from odoo import api, fields, models

# classical inheritance

class PatientGuardian(models.Model):
    _inherit = "hospital.patient"

    guardian_name = fields.Char(string="Guardian Name")
    guardian_relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('spouse', 'Spouse'),
        ('sibling', 'Sibling'),
        ('other', 'Other'),
    ], string="Relation")
    guardian_contact = fields.Char(string="Contact Number")
    guardian_address = fields.Text(string="Address")
