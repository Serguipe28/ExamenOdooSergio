from odoo import models, fields, api

class estudiante(models.Model):
    
    _inherit = 'wallaport.persona'
    _name = 'wallaport.estudiante'
    _description = 'Estudiantes'
    
    
    #Relaciones entre tablas
    portatiles_id = fields.One2many('wallaport.portatil', 'estudiante_id', string='Id de los portatiles')
    
    