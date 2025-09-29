from odoo import api, fields, models

class ExamsSubject(models.Model):
    _name = "exams.subjects"
    _description = "Subjects"

    name = fields.Char(string="Name", required=True)
    exam_ids = fields.One2many('exams.exam','subject_id',string="Exams")
