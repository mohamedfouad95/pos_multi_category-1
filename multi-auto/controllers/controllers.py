# -*- coding: utf-8 -*-
from odoo import http

# class Multi-auto(http.Controller):
#     @http.route('/multi-auto/multi-auto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi-auto/multi-auto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi-auto.listing', {
#             'root': '/multi-auto/multi-auto',
#             'objects': http.request.env['multi-auto.multi-auto'].search([]),
#         })

#     @http.route('/multi-auto/multi-auto/objects/<model("multi-auto.multi-auto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi-auto.object', {
#             'object': obj
#         })