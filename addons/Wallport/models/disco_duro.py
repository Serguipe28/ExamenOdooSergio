from odoo import models, fields, api

class disco_duro(models.Model):
    _name = 'wallaport.disco_duro'
    _description = 'Disco Duro'
    
    
    tamano = fields.Char(string='Tamano del disco duro')
    tipo = fields.Selection(string='Tipo de disco', selection=[('h', 'hdd'),('s', 'ssd'), ('n', 'nvme')])
    
    #Relaciones entre tablas
    portatil_id = fields.Many2one('wallaport.portatil', string='Id portatil')