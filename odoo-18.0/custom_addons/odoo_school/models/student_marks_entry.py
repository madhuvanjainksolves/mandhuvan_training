from odoo import models, fields, api

class MarksEntry(models.Model):
    _name = "school.marks.entry"
    _description = "Marks Entry"

    class_id = fields.Many2one("school.class", string="Class", required=True)
    subject_id = fields.Many2one("school.subject", string="Subject", required=True)
    marks_ids = fields.One2many("school.student.marks", "marks_entry_id", string="Marks")
    name = fields.Char(string="Class_Subject", compute="_compute_name", store=True)

    @api.depends('class_id', 'subject_id')
    def _compute_name(self):
        for rec in self:
            rec.name = (rec.class_id.name or "") + "_" + (rec.subject_id.name or "")
