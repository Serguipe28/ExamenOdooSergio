from odoo import models, fields, api

class Ofertas(models.Model):
    _name = 'wallaport.ofertas'
    _description = 'Ofertas'
    
    observaciones = fields.Text(string='Observaciones')
    #Relaciones entre tablas
    portatil_id = fields.Many2one('wallaport.portatil', string='Id portatil')
    comprador_id = fields.Many2one('wallaport.comprador', string='Id comprador')