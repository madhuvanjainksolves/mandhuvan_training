from odoo import http
from odoo.http import request


class HelloController(http.Controller):
    @http.route('/hello', type = 'http', website=True)
    def printhello(self):
        return "hello"

class SchoolReportController(http.Controller):

    @http.route('/school/report/marks', type='http', auth='public', website=False)
    def marks_report(self, **kw):
        marks = request.env['school.student.marks'].search([])
        data = []
        for mark in marks:
            data.append({
                "student": mark.student_id.name,
                "class": mark.student_id.class_id.name if mark.student_id.class_id else "",
                "subject": mark.subject_id.name if mark.subject_id else "",
                "marks": mark.marks,
            })
        return request.make_response(str(data))
