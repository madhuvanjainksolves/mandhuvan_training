from odoo import models, fields, api
from datetime import date

class ExamCreationWizard(models.TransientModel):
    _name = "exams.creation.wizard"
    _description = "Wizard to Create Exams"

    exam_date = fields.Date(
        string="Exam Date",
        required=True,
        default=lambda self: date.today()
    )

    def create_exams(self):
        students = self.env['exams.students'].search([])
        subjects = self.env['exams.subjects'].search([])

        student_ids = students.ids
        subject_ids = subjects.ids

        exams_to_create = [
            {
                'student_id': s_id,
                'subject_id': sub_id,
                'marks': 0,
                'exam_date': self.exam_date
            }
            for s_id in student_ids
            for sub_id in subject_ids
        ]

        if exams_to_create:
            created_records = self.env['exams.exam'].create(exams_to_create)

            return {
                'name': 'Created Exams',
                'type': 'ir.actions.act_window',
                'res_model': 'exams.exam',
                'view_mode': 'list,form',
                'domain': [('id', 'in', created_records.ids)],
                'context': self.env.context,
            }

        return {'type': 'ir.actions.act_window_close'}
