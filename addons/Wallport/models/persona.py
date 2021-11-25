from odoo import models, fields, api

class persona(models.Model):
    _name = 'wallaport.persona'
    _description = 'persona'
    
    dni = fields.Char(string='DNI', size=9)
    name_lastname = fields.Char(string='Nombre y apellidos')
    address = fields.Text(string='Direccion')
    phone_number = fields.Char(string='Telenfon')
    
    
    