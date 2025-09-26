{
    "name": "Odoo Teacher",
    "version": "1.0.0",
    "Sequence": 1,
    "summary": "odoo teacher module is depends on hr module. In this i added add a few new fields in the hr_employee model and use it as a teacher. ",
    "category": "Education",
    "author": "Madhuvan Jain",
    "depends": ["hr"],
    "data": [
        "views/hr_employee_views.xml",
        "views/menus.xml",
        "school_class_views.xml",
    ],
    "installable": True,
    "application": True,
    'license': 'LGPL-3',
}

