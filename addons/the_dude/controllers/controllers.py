 #-*- coding: utf-8 -*-
from odoo import http


class TheDude(http.Controller):
     @http.route('/the_dude/the_dude', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/the_dude/the_dude/objects', auth='public')
     def list(self, **kw):
         return http.request.render('the_dude.listing', {
             'root': '/the_dude/the_dude',
             'objects': http.request.env['the_dude.the_dude'].search([]),
         })

     @http.route('/the_dude/the_dude/objects/<model("the_dude.the_dude"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('the_dude.object', {
             'object': obj
         })

