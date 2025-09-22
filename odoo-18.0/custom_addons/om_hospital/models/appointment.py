from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name="patient_id"
    _order = "appointment_time desc"

    patient_name = fields.Char(string="Patient Name")
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

    def action_confirm(self):
        """Confirm the appointment"""
        for rec in self:
    #         # Fetch all patients
    #         patients = self.env["hospital.patient"].search([])
    #         print("patients ..", patients)
    #         # Fetch female patients
    #         femalepatients = self.env["hospital.patient"].search([('gender', '=', 'female'),('age', '>', '21')])
    #         print("female patients.... ", femalepatients)
    #         # using or
    #         femalepatientsor = self.env["hospital.patient"].search(['|', ('gender', '=', 'female'),('age', '>', '21')])
    #         print("female patients or .... ", femalepatientsor)
    #         # Fetch female patients
    #         malepatients = self.env["hospital.patient"].search([('gender', '=', 'male')])
    #         print("male patients.... ", malepatients)
    #         # count patient
    #         patients_count = self.env["hospital.patient"].search_count([])
    #         print("patient count ", patients_count)
    #
    #
    #         # ref in odoo
    #         om_patient = self.env.ref('__custom__.palak')
    #         print("om patient:", om_patient.id)
    #         # browse
    #         browser_result = self.env["hospital.patient"].browse(29)
    #         print("browser_result" , browser_result.name)
    #         print("browser_result", browser_result.name_seq)
    #         # difference in browse and search
    #         brower_search = self.env["hospital.patient"].search([('id', '=', '200')])
    #         print("result in search.... ", brower_search)
    #         # using exists
    #         browser_result_exists = self.env["hospital.patient"].browse(220)
    #         if browser_result_exists.exists():
    #             print("yes in DB")
    #         else:
    #             print("noooooooooooo")

            # create and update
            # vals = {
            #     'name': 'satya jain',
            #     'email' : 'satyajain567@gmail.com',
            #     'phone' : '910393807112',
            #     'gender': 'female',
            #     'age' : '25'
            # }
            # created_record = self.env['hospital.patient'].create(vals)
            #
            # record_to_update = self.env['hospital.patient'].browse(29)
            # if record_to_update.exists():
            #     vals = {
            #         'name': 'aditi jain',
            #         'email': 'aditijain567@gmail.com',
            #     }
            #     record_to_update.write(vals)

            #copy
            # record_to_copy = self.env['hospital.patient'].browse(29)
            # record_to_copy.copy()

            # unlink
            # record_to_unlink = self.env['hospital.patient'].browse(31)
            # record_to_unlink.unlink()


            rec.state = 'confirmed'



    def action_cancel(self):
        """Cancel the appointment"""
        self.state = 'cancelled'

    def action_create_patient(self):
        for appointment in self:
            if not appointment.patient_name:
                raise ValidationError("Please enter a patient name before creating a patient.")

            # Check if patient with this name already exists
            existing_patient = self.env['hospital.patient'].search([('name', '=', appointment.patient_name)], limit=1)
            if existing_patient:
                raise ValidationError(f"A patient with the name '{appointment.patient_name}' already exists!")

            # Create new patient
            new_patient = self.env['hospital.patient'].create({
                'name': appointment.patient_name
            })

            # Assign the created patient to appointment
            appointment.patient_id = new_patient.id
        return True
