from odoo import models, fields

class PatientInsurance(models.Model):
    _name = "hospital.patient.insurance"
    _description = "Patient Insurance"
    _inherits = {"hospital.patient": "patient_id"}  # delegation inheritance

    patient_id = fields.Many2one(
        "hospital.patient",
        string="Patient",
        required=True,
        ondelete="cascade"
    )
    insurance_company = fields.Char(string="Insurance Company")
    policy_number = fields.Char(string="Policy Number")
    coverage_amount = fields.Float(string="Coverage Amount")
    expiry_date = fields.Date(string="Expiry Date")