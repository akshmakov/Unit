# -*- coding: utf-8 -*-
from odoo import http

# class Digi(http.Controller):
#     @http.route('/digi/digi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digi/digi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('digi.listing', {
#             'root': '/digi/digi',
#             'objects': http.request.env['digi.digi'].search([]),
#         })

#     @http.route('/digi/digi/objects/<model("digi.digi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digi.object', {
#             'object': obj
#         })