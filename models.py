# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Car(models.Model):
    _name ='creditcalc.car'

    name = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year", required=True)
    kms = fields.Float(string="kms", required=True)
    price = fields.Float(string="Price", required=True)
    owner_id = fields.Many2one('res.partner', ondelete='cascade', string="Owner", required=False)
    sold = fields.Boolean(default=False, readonly="True")

class Contract(models.Model):
    _name = 'creditcalc.contract'

    date = fields.Date(default=fields.Date.today)

    rate = fields.Float(string="Credit rate")

    term = fields.Selection([
        ('1', "1 month"),
        ('2', "2 months"),
        ('3', "3 months"),
        ('4', '4 months'),
        ('5', "5 months"),
        ('6', "6 months"),
        ('7', '7 months'),
        ('8', "8 months"),
        ('9', "9 months"),
        ('10', '10 months'),
        ('11', "11 months"),
        ('12', "12 months"),
    ],String="Term of contract", required=True)

    deposit = fields.Float(string="Deposit", required=True)
    sum = fields.Float(string="Sum of contract")
    car_id = fields.Integer(required=True)
    customer_id = fields.Many2one('res.partner', ondelete='cascade', string="Customer", required=False)
    state = fields.Selection([
        ('new', "New"),
        ('signed', "Signed"),
        ('expired', "Expired"),
        ('canceled', 'Canceled'),
    ],string="State of contract", default="new")

class BaseRate(models.Model):
    _name = 'creditcalc.rate'

    date = fields.Date(default=fields.Date.today)
    rate = fields.Float(required=True)