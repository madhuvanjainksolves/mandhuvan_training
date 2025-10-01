from odoo import models, fields

class MarksReportWizard(models.TransientModel):
    _name = "marks.report.wizard"
    _description = "Marks Report Wizard"

    class_id = fields.Many2one("school.class", string="Class", required=True)
    subject_id = fields.Many2one("school.subject", string="Subject", required=True)

    def action_generate_report(self):
        marks = self.env['school.student.marks'].search([
            ('student_id.class_id', '=', self.class_id.id),
            ('marks_entry_id.subject_id', '=', self.subject_id.id),
        ])

        return self.env.ref('odoo_school.marks_report_pdf').report_action(
            self,
            data={
                'marks_ids': marks.ids,
                'class_name': self.class_id.name,
                'subject_name': self.subject_id.name,
            }
        )
