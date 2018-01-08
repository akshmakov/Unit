# -*- coding: utf-8 -*-
from odoo import models, fields, api

class unit(models.Model):
    _name = 'unit.unit'
    _description = 'Unit'

    name = fields.Char()
    description = fields.Text()

    sn = fields.Char()
    pn = fields.Char()

    inventory_status_id = fields.Many2one('unit.unit_status')

    record_ids = fields.One2many('unit.record', 'unit_id')
    event_ids = fields.One2many('unit.event', 'unit_id')
    

    
