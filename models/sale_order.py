# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderPersonalization(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_create_invoice_auto(self):
        self.ensure_one()
        self.action_invoice_create()
        return self.action_view_invoice()

    @api.multi
    def action_confirm(self):
        # Add code here
        for so in self:
            so.name = so.name.replace("SO", "PV")
            so.name = so.name.replace("PRE", "PV")
        return super(SaleOrderPersonalization, self).action_confirm()
