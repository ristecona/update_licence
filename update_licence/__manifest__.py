# -*- coding: utf-8 -*-
{
    'name': "update_licence",

    'summary': """
        Update the expiration date of the instance so that the db will not expire, ever! DO a sudo apt-get install python-dateutil
 before using the module""",

    'description': """
        Update the expiration date of the instance so that the db will not expire, ever!
    """,

    'author': "Unknown",
    'website': "http://www.unknown.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'base',
    'version': '0.1',
    'price': 299,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}