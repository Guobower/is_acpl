# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_date_intervention = fields.Char(string="Date(s) d'intervention(s)")
    is_type_facture      = fields.Selection([
        ('atelier', u'Atelier'),
        ('controle-analogique', u'Contrôle analogique'),
        ('controle-numerique' , u'Contrôle numérique')
    ], "Type de facture", required=True, default='atelier')
