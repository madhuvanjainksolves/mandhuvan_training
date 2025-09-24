from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError
# from odoo.tools import lazy_property

class HospitalPatient(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _order = "name"

    name = fields.Char(string="Name", tracking=True, required=True)
    age = fields.Integer(string="Age", compute="_compute_age", inverse= "_inverse_age" ,store = True, tracking=True)
    ref = fields.Char(string="Reference", default="madhuvan jain")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    date_of_birth = fields.Date(string="Date of Birth")
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('admitted', 'Admitted'),
            ('discharged', 'Discharged'),
        ],
        string="Status",
        default="draft",
        tracking=True
    )

    blood_group = fields.Selection(
        [('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),
         ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')],
        string="Blood Group"
    )
    phone = fields.Char(string="Phone Number")
    email = fields.Char()
    address = fields.Text(string="Address")
    name_seq = fields.Char( string="Patient ID", required=True, copy=False, readonly=True, default=lambda self: self.env["ir.sequence"].next_by_code("hospital.patient"),)

    # compute method for age
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year - (
                        (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day)
                )
            else:
                rec.age = 0

    def _inverse_age(self):
        for rec in self:
            if rec.age:
                today = date.today()
                rec.date_of_birth = today.replace(year=today.year - rec.age)

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            # Only check if age is set
            if rec.age and rec.age <= 0:
                raise ValidationError("Age is incorrect")

    _sql_constraints = [
        ('unique_phone', 'UNIQUE(phone)', 'The phone number must be unique for each patient!')
    ]

    # One2many
    appointment_ids = fields.One2many("hospital.appointment", "patient_id", string="Appointments")
    appointment_count = fields.Integer(string="Appointments", compute="_compute_appointment_count")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for patient in self:
            patient.appointment_count = len(patient.appointment_ids)

    def action_view_appointments(self):
        self.ensure_one()
        return {
            'name': 'Appointments',
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointment',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
        }


#     name get function and @api.model
    @api.model
    def create(self, vals):
        if vals.get('name_seq', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'
        return super(HospitalPatient, self).create(vals)

    def name_get(self):
        result = []
        for record in self:
            display_name = '%s - %s' % (record.name, record.name_seq)
            result.append((record.id, display_name))
        return result




