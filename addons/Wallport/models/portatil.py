from odoo import models, fields, api

class Portatil(models.Model):
    _name = 'wallaport.portatil'
    _description = 'Portatil'
    
    modelo = fields.Char(string='Modelo')
    marca = fields.Char(string='Marca')
    cpu = fields.Char(string='CPU')
    fecha = fields.Date(string='Fecha de adquisicion')
    tiempo_uso = fields.Float(string='Tiempo de uso', digits=(12, 30))
    precio = fields.Float(string='Precio de venta')
    observaciones = fields.Text(string='Campo de observaciones')
    vendido = fields.Boolean(string='vendido')
    
    #Relaciones entre tablas
    estudiante_id = fields.Many2one('wallaport.estudiante', string='Id estudiante')
    ram_id = fields.One2many('wallaport.ram', 'portatil_id', string='Id ram')
    disco_id = fields.One2many('wallaport.disco_duro', 'portatil_id', string='Disco duro id')
    ofertas_id = fields.One2many('wallaport.ofertas', 'portatil_id', string='Id de las ofertas')
    
    
    
    

    # ram_total = fields.Char(compute='_compute_ram_total', string='')
    
    # @api.depends('ram_id')
    # def _compute_ram_total(self):
    #     for r in self:
    #         r.ram_total = "ram: %" % r.ram_id
            

    #3.11
    #3.12
    #3.13
    #3.14
    #3.15