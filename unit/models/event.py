# -*- coding: utf-8 -*-
from odoo import models, fields, api

class event(models.Model):
    _name = 'unit.event'
    _description = "Unit Event"
    
    
    
    _type = fields.Char()

    location = fields.Many2one('unit.location')
    unit_id = fields.Many2one('unit.unit')
    comment = fields.Text("Event Comment")

    record_ids = fields.One2many('unit.record', 'event_id')
    
    


class unit_status(models.Model):
    _name = 'unit.unit_status'
    _description = "Unit Status"

    name = fields.Char("Name", index=True)
    short = fields.Char("StatusCode", index = True)
    description = fields.Text("Description")

    allowed_outgoing_ids = fields.Many2many('unit.unit_status','legal_status_changes', 'from_status', 'to_status')

    
    

    
