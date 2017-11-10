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
        'security/ir.model.access.csv',
        'views/assets.xml',
        'report/conditions_generales_de_vente_templates.xml',
        'report/sale_report_templates.xml',
        'views/account_invoice_view.xml',
        'views/report_invoice.xml',
        'views/sale_view.xml',
        'views/partner_view.xml',
        'views/is_export_compta_view.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

