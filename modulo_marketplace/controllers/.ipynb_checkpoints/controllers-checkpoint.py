# -*- coding: utf-8 -*-
from odoo import http

# class ModuloMarketplace(http.Controller):
#     @http.route('/modulo_marketplace/modulo_marketplace/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_marketplace/modulo_marketplace/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_marketplace.listing', {
#             'root': '/modulo_marketplace/modulo_marketplace',
#             'objects': http.request.env['modulo_marketplace.modulo_marketplace'].search([]),
#         })

#     @http.route('/modulo_marketplace/modulo_marketplace/objects/<model("modulo_marketplace.modulo_marketplace"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_marketplace.object', {
#             'object': obj
#         })

class ModuloMarketplace(http.Controller):
    @http.route('/modulo_marketplace/modulo_marketplace/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/modulo_marketplace/modulo_marketplace/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('modulo_marketplace.listing', {
            'root': '/modulo_marketplace/modulo_marketplace',
            'objects': http.request.env['modulo_marketplace.modulo_marketplace'].search([]),
        })

    @http.route('/modulo_marketplace/modulo_marketplace/objects/<model("modulo_marketplace.modulo_marketplace"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('modulo_marketplace.object', {
            'object': obj
        })