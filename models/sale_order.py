# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import pdb


class SaleOrderPersonalization(models.Model):
    _inherit = "sale.order"

    payment_count = fields.Integer(compute="count_payments")

    @api.one
    @api.depends('payment_count')
    def count_payments(self):
        payments = self.env['account.payment'].search([('sale_order_id', '=', self.id)])
        self.payment_count = len(payments.ids)

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

    @api.multi
    def action_add_payment(self):
        context = {'default_payment_type': 'inbound',
                   'default_partner_type': 'customer',
                   'default_communication': 'ANTICIPO: '+str(self.name),
                   'default_partner_id': self.partner_id.id,
                   'default_payment_method_id': self.env.ref('account.account_payment_method_manual_in').id,
                   'default_sale_order_id': self.id,
                   }
        return {'name': _('Payments'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'account.payment',
                'view_id': self.env.ref('am_personalizations.view_account_payment_sale_order').id,
                'type': 'ir.actions.act_window',
                'context': context,
                'target': 'new'
                }


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
                ('code', '=', 'incoming')],
                limit=1).id
