

{
    "name": 'Hospital Management',
    "author": "Mohamed BA",
    "category": 'Hospital',
    'sequence': -100,
    "summary":"Hospital Managment Systême",
    "version": '1.0.0',
    'Descriptions':'***** Hospital Managment Systême *****',
    "depends": [
        'mail',
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_view.xml",
        "views/female_patient_view.xml",
        "views/appointment_view.xml",
    ],
    'demo': [],
    'auto_instale': False,
    'application': True,
    'license': 'LGPL-3',
}
