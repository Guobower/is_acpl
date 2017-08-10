# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_lieu_intervention = fields.Char(string="Lieu d'intervention")


