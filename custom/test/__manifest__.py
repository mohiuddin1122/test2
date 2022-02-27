{
    'name': 'om_hospital',
    'author': 'Muhammad Mohiuddin',
    'version': '1.1',
    'summary': 'Management Software',
    'sequence': -100,
    'description': """Management Software""",
    'category': 'Productivity',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['sale', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'views/patient.xml',
        'views/kids_view.xml',
        'views/appointment_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
