 #-*- coding: utf-8 -*-

from odoo import models, fields, api


class estudiantes(models.Model):
     _name = 'estudiantes.estudiantes'
     _description = 'estudiantes.estudiantes'

     alumno = fields.Char()
     nivel_sueno = fields.Integer(required = True, default = 1, string="Nivel de sueño(1-10")
     bebida_recomendada = fields.Char(compute = "_compute_nivel_sueno",store=True)

     @api.depends('nivel_sueno')
     def _compute_nivel_sueno(self):
         for record in self:
             nivel = record.nivel_sueno

            if nivel < 3:
                record.bebida_recomendada = "Cafe con leche"
