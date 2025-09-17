from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name="patient_id"

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('cancelled', 'Cancelled')],
        string="Status", default="draft", tracking=True
    )
    description = fields.Text(string="Reason for Visit / Notes")

    ref = fields.Char(string="Reference", default="madhuvan jain")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    # Many2one
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    gender = fields.Selection(string="Gender", related="patient_id.gender")
    appointment_time = fields.Datetime(string='Appointment Time', default = fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)

    # Many2many
    doctor_ids = fields.Many2many("hospital.doctor", "hospital_doctor_appointment_rel", "appointment_id", "doctor_id", string="Doctors")

