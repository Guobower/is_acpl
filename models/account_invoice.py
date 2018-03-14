# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_date_intervention = fields.Char(string="Date(s) d'intervention(s)")
    is_type_facture      = fields.Selection([
        ('atelier', u'Atelier'),
        ('controle-analogique', u'Contrôle analogique'),
        ('controle-numerique' , u'Contrôle numérique'),
        ('divers', u'Divers'),
    ], "Type de facture", required=True, default='atelier')




class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"
    _order = "invoice_id,id"

    is_num_controle = fields.Char(string="N° du contrôle")


