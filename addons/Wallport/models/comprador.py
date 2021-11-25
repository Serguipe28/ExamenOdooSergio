from odoo import models, fields, api

class comprador(models.Model):
    _inherit = 'wallaport.persona'
    _name = 'wallaport.comprador'
    _description = 'Comprador'
    
    
    #Relaciones entre tablas
    ofertas_id = fields.One2many('wallaport.ofertas','comprador_id', string='Id de las ofertas')
    
    