# -*- coding: utf-8 -*-
from odoo import http

# class UpdateLicence(http.Controller):
#     @http.route('/update_licence/update_licence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_licence/update_licence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_licence.listing', {
#             'root': '/update_licence/update_licence',
#             'objects': http.request.env['update_licence.update_licence'].search([]),
#         })

#     @http.route('/update_licence/update_licence/objects/<model("update_licence.update_licence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_licence.object', {
#             'object': obj
#         })