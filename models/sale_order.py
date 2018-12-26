# -*- coding: utf-8 -*-

from odoo import models, fields, api
import pdb

class ResUsers(models.Model):
    _inherit = "res.users"

    default_warehouse = fields.Many2one("stock.warehouse", "Almacén por defecto")


class SaleOrderPersonalization(models.Model):
    _inherit = "sale.order"

    @api.onchange('warehouse_id')
    def onchange_method(self):
        if self.env.user.default_warehouse.id:
            self.warehouse_id = self.env.user.default_warehouse.id

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

