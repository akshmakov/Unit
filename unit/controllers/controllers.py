# -*- coding: utf-8 -*-
from odoo import http

class Unit(http.Controller):
  
  @http.route('/unit/unit/', auth='public')
  def index(self, **kw):
    return "Hello, world"
  
  @http.route('/unit/unit/objects/', auth='public')
  def list(self, **kw):
    return http.request.render('unit.listing', {
      'root': '/unit/unit',
      'objects': http.request.env['unit.unit'].search([]),
    })
  
  @http.route('/unit/unit/objects/<model("unit.unit"):obj>/', auth='public')
  def object(self, obj, **kw):
    return http.request.render('unit.object', {
      'object': obj
    })

  
  
class Event(http.Controller):
  @http.route('/unit/event/', auth='public')
  def index(self, **kw):
    return "Hello, world"

  @http.route('/unit/event/objects/', auth='public')
  def list(self, **kw):
    return http.request.render('unit.listing', {
      'root': '/unit/event',
      'objects': http.request.env['unit.event'].search([]),
    })
  
  @http.route('/unit/event/objects/<model("unit.event"):obj>/', auth='public')
  def object(self, obj, **kw):
    return http.request.render('unit.object', {
      'object': obj
    })
  
     
class Record(http.Controller):
  @http.route('/unit/record/', auth='public')
  def index(self, **kw):
    return "Hello, world"
  
  @http.route('/unit/record/objects/', auth='public')
  def list(self, **kw):
    return http.request.render('unit.listing', {
      'root': '/unit/record',
      'objects': http.request.env['unit.record'].search([]),
        })
  
  @http.route('/unit/record/objects/<model("unit.record"):obj>/', auth='public')
  def object(self, obj, **kw):
    return http.request.render('unit.object', {
      'object': obj
    })
  
