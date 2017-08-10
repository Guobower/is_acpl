# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo pour ACPL',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône/ACPL',


    'description': """
InfoSaône - Module Odoo pour ACPL
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale',
        'mail',
        'account',
        'account_accountant',
        'purchase',
        'document',
],
    'data' : [
        'views/report_invoice.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

