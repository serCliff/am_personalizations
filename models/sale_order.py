# -*- coding: utf-8 -*-

from odoo import models, fields, api
import pdb


class ResUsers(models.Model):
    _inherit = "res.users"

    default_warehouse = fields.Many2one("stock.warehouse", "Almacén por defecto")


class SaleOrderPersonalization(models.Model):
    _inherit = "sale.order"


    @api.onchange('user_id')
    def change_warehouse(self):
        """
            Establece el almacén que tenga el usuario que genera la venta por defecto
        """
        if self.env.user.default_warehouse.id:
            self.warehouse_id = self.user_id.default_warehouse.id

    @api.multi
    def action_create_invoice_auto(self):
        """
        Botón para crear la factura directamente sin opciones (adelantos...)
        """
        self.ensure_one()
        self.action_invoice_create()
        return self.action_view_invoice()

    @api.multi
    def action_confirm(self):
        """
        Cambia el nombre de la factura en el momento de confirmación
        """
        for so in self:
            so.name = so.name.replace("SO", "PV")
            so.name = so.name.replace("PRE", "PV")
        return super().action_confirm()



class SaleOrderPersonalization(models.Model):
    _inherit = "purchase.order"

    user_id = fields.Many2one("res.users", "Responsable", default=lambda self: self.env.user.id)

    @api.onchange('user_id')
    def onchange_method(self):
        """
            Establece el almacén que tenga el usuario que genera la compra por defecto
        """
        if self.env.user.default_warehouse.id:
            self.picking_type_id = self.env['stock.picking.type'].search([
                ('warehouse_id', '=', self.user_id.default_warehouse.id),
                ('code','=','incoming')],
                limit=1).id
