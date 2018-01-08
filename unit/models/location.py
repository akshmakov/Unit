from odoo import models, fields, api




class company(models.Model):
    _name = 'unit.company'
    _description = 'Unit Company'
    name = fields.Char("Company Name")
    contacts = fields.One2many('unit.contact','company_id')

class contact(models.Model):
    _name = 'unit.contact'
    _description = 'Unit Contact'
    name = fields.Char("Company Contact")
    company_id = fields.Many2one('unit.company')
    locations_ids = fields.Many2many('unit.location')
    
class location(models.Model):
    _name = 'unit.location'
    _description = 'Unit Location'
    name = fields.Char("Location Name")
    company_id = fields.Many2one('unit.company')
    contact_ids = fields.Many2many('unit.contact')
    parent_id = fields.Many2one('unit.location')
    children_ids = fields.Many2one('unit.location', 'parent_id')
    

