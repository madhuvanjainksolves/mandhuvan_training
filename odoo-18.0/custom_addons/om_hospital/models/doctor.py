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

    user_id = fields.Many2one(
        'res.users',
        string="Related User"
    )

    appointment_ids = fields.Many2many(
        "hospital.appointment",
        "hospital_doctor_appointment_rel",
        "doctor_id",
        "appointment_id",
        string="Appointments"
    )

    @api.model
    def create(self, vals):
        # Create the doctor record first
        doctor = super(HospitalDoctor, self).create(vals)

        # If no user is linked, create one automatically
        if not doctor.user_id:
            # Create a user for this doctor
            group_doctor = self.env.ref('om_hospital.group_hospital_doctor')  # your doctor group
            user_vals = {
                'name': doctor.name,
                'login': doctor.email or doctor.name.replace(" ", "").lower(),
                'email': doctor.email or "",
                # 'groups_id': [(4, group_doctor.id)],
                'password': "doctor123",  # default password (ask them to change later)
            }
            user = self.env['res.users'].create(user_vals)

            # Link user to doctor
            doctor.user_id = user.id

        return doctor