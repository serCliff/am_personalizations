# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = "res.users"

    default_warehouse = fields.Many2one("stock.warehouse", "Almacén por defecto")


class ResPartnerPersonalization(models.Model):
    _inherit = "res.partner"

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for partner in self:
            partner.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'res.partner'), ('res_id', '=', partner.id)
            ])

    remaining_battery = fields.Integer("Pilas Restantes")
    born_date = fields.Date("Fecha de Nacimento")

    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")
    rgpd_signed = fields.Boolean(string="Firmar RGPD", default=False)
    rgpd_signature = fields.Binary(string="Firma", attachment=True)

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '&', ('res_model', '=', 'res.partner'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                            Documents are attached to your partner.</p><p>
                            Send messages or log internal notes with attachments to link
                            documents to your partner.
                        </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

