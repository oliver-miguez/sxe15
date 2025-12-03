 #-*- coding: utf-8 -*-

from odoo import models, fields, api


class estudiantes(models.Model):
     _name = 'estudiantes.estudiantes'
     _description = 'estudiantes.estudiantes'

     alumno = fields.Char()
     nivel_sueno = fields.Integer(required = True, default = 1, string="Nivel de sueño(1-10)")
     bebida_recomendada = fields.Char(compute = "_compute_nivel_sueno",store=True) # Utilizamos esto para poder definir el nivel de sueño y su bebida correspondiente

     @api.depends('nivel_sueno')
     def _compute_nivel_sueno(self):
         for record in self:
             nivel = record.nivel_sueno

            # Definir que efecto produce cada bebida
             if 3 >= nivel >= 0:
                 record.bebida_recomendada = "Leche con café"
             elif 4 <= nivel <= 6:
                 record.bebida_recomendada = "Largo solo"
             elif 7 <= nivel <= 9:
                 record.bebida_recomendada = "Largo no, lo siguiente"
             elif nivel == 10:
                 record.bebida_recomendada = " CHUTE DE ADRENALINAAAAA"
             elif nivel > 10:
                 record.bebida_recomendada = "Bebes tanto cafe y redbull que mueres"
             elif nivel < 0:
                 record.bebida_recomendada = "No bebes nada"