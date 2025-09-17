from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError
# from odoo.tools import lazy_property

class HospitalPatient(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True, required=True)
    age = fields.Integer(string="Age", compute="_compute_age", inverse= "_inverse_age" ,store = True, tracking=True)
    ref = fields.Char(string="Reference", default="madhuvan jain")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, required=True)
    active = fields.Boolean(string="Active", default=True)
    date_of_birth = fields.Date(string="Date of Birth")

    blood_group = fields.Selection(
        [('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),
         ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')],
        string="Blood Group"
    )
    phone = fields.Char(string="Phone Number")
    email = fields.Char()
    address = fields.Text(string="Address")

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
            if rec.age <= 0 :
                raise ValidationError("age is incorrect ")

    _sql_constraints = [
        ('unique_phone', 'UNIQUE(phone)', 'The phone number must be unique for each patient!')
    ]

    # One2many
    appointment_ids = fields.One2many("hospital.appointment", "patient_id", string="Appointments")

