# -*- coding: utf-8 -*-
from openerp import http

# class Creditcalc(http.Controller):
#     @http.route('/creditcalc/creditcalc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/creditcalc/creditcalc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('creditcalc.listing', {
#             'root': '/creditcalc/creditcalc',
#             'objects': http.request.env['creditcalc.creditcalc'].search([]),
#         })

#     @http.route('/creditcalc/creditcalc/objects/<model("creditcalc.creditcalc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('creditcalc.object', {
#             'object': obj
#         })