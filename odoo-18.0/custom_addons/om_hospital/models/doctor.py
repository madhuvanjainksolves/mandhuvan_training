from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"

    name = fields.Char(string="Doctor Name")
    speciality = fields.Char(string="Speciality")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    available_days = fields.Char(string="Available Days")
    # many2many

    appointment_ids = fields.Many2many("hospital.appointment", "hospital_doctor_appointment_rel", "doctor_id", "appointment_id", string="Appointments")
