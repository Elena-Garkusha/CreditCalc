# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Car(models.Model):
    _name ='creditcalc.car'

    name = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year", required=True)
    kms = fields.Float(required=True)
    owner_id = fields.Many2one('res.partner', ondelete='cascade', string="Owner", required=True)
    sold = fields.Boolean(default=False)

class Owner(models.Model):
    _inherit = 'res.partner'

    car_ids = fields.One2many('creditcalc.car', 'owner_id', string="Car")

class Customer(models.Model):
    _inherit = 'res.partner'

    # contract_ids = fields.One2many()

class Contract(models.Model):
    _name = 'creditcalc.contract'

    date = fields.Date(default=fields.Date.today)
    # rate = fields.Many2one()
    term = fields.Integer(string="Term of contract", required=True)
    deposit = fields.Float(string="Deposit", required=True)
    car_id = fields.Integer(required=True)
    # customer_id = fields.Many2one()
    state = fields.Char(default="new")

class BaseRate(models.Model):
    _name = 'creditcalc.rate'

    date = fields.Date(default=fields.Date.today)
    rate = fields.Float(required=True)