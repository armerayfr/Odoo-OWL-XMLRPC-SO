# -*- coding: utf-8 -*-
{
    'name': "AR Invoice Request",

    'summary': """
        Invoice Request""",

    'description': """
        Used to Request INV
    """,

    'author': "Armer Ray",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/external_template_wrapper.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'ar_invoice_request/static/src/xml/external_invoice_template.xml',
            'ar_invoice_request/static/src/js/external_invoice_form.js',
            'ar_invoice_request/static/src/js/main.js',
        ],
    },

}
