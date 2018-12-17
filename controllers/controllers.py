# -*- coding: utf-8 -*-
from odoo import http

# class AmPersonalizations(http.Controller):
#     @http.route('/am_personalizations/am_personalizations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/am_personalizations/am_personalizations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('am_personalizations.listing', {
#             'root': '/am_personalizations/am_personalizations',
#             'objects': http.request.env['am_personalizations.am_personalizations'].search([]),
#         })

#     @http.route('/am_personalizations/am_personalizations/objects/<model("am_personalizations.am_personalizations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('am_personalizations.object', {
#             'object': obj
#         })