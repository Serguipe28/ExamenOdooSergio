from odoo import models, fields, api

class ram(models.Model):
    _name = 'wallaport.ram'
    _description = 'Ram del portatil'
    
    frecuencia = fields.Char(string='Frecuencia')
    latencia = fields.Char(string='Latencia')
    cantidad = fields.Float(string='Cantidad en gb')
    modulo = fields.Selection(string='Tipo de modulo', selection=[('3', 'dd3'),('4', 'dd4'), ('5', 'dd5')])
    
    #Relaciones entre tablas
    portatil_id = fields.Many2one('wallaport.portatil', string='Id del portatil')
    