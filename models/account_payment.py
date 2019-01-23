# -*- coding: utf-8 -*-

from odoo import models, fields, api

import pdb;


class AccountPaymentPersonalization(models.Model):
    _inherit = "account.payment"

    sale_order_id = fields.Many2one('sale.order')


    @api.multi
    def action_validate_invoice_payment(self):
        """
            Si la factura queda totalmente pagada y no se ha validado el albarán de salida lo confirma
        """
        inv = self.env['account.invoice'].browse(self._context.get('active_id'))
        if inv.residual - self.amount == 0:
            pv_name = inv.origin
            if pv_name:
                stock_picking = self.env['stock.picking'].search([('origin', '=', pv_name)])
                for picking in stock_picking:
                    if picking.state != 'done':
                        for line in picking.move_lines:
                            line.quantity_done = line.product_uom_qty
                            line.env.cr.commit()
                        picking.button_validate()
        return super(AccountPaymentPersonalization, self).action_validate_invoice_payment()
