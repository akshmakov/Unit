# -*- coding: utf-8 -*-
from odoo import models, fields, api


class record(models.Model):
    _name = 'unit.record'

    location = fields.Many2one('unit.location')
    unit_id = fields.Many2one('unit.unit')
    event_id = fields.Many2one('unit.event')
    comment = fields.Text("Comment")
    attachment_ids = fields.One2many('unit.record_attachment','record_id')


class record_attachment(models.Model):
    _name = 'unit.record_attachment'

    record_id = fields.Many2one('unit.record')
    data = fields.Binary("Attachment Data")
    

    
