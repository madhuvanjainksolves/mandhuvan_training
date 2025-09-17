# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'hospital management',
    'version': '1.0.0',
    'sequence': '-100',
    'category': 'Hospital management ',
    'author': 'Madhuvan Jain',
    'summary': 'Hospital management system',
    'description': """It is a module that is use for hospital management/n""",
    'depends': ['mail'],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_views.xml",
        "views/female_patient_views.xml",
        "views/appointment_views.xml",
        "views/doctor_view.xml",],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
