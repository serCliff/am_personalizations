# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
# from odoo.tools import report


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
    communication_rgpd = fields.Boolean(string="Comunicación", default=True, help="Autoriza todo tipo de información referente a los servicios que presta, comunicaciones de cortesía, comunicaciones comerciales, ofertas, promociones,etc.")
    photo_rgpd = fields.Boolean(string="Realización de fotografías", default=True, help="Autoriza expresamente a que el RT pueda realizarle fotografías y/o reportajes de vídeo de su participación en el evento organizado por el RT")
    medical_report_rgpd = fields.Boolean(string="Envío de informes médicos", default=True, help="Autoriza expresamente al RT al envío de los informes médicos del titular de los datos, a los familiares del mismo")

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



        # @api.multi
    # def action_print(self):
    #     return self.env.ref('am_personalizations.rgpd_signed').report_action(self)

        # return self.env['report'].get_action(self, 'am_personalizations.rgpd_signed')

