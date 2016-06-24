# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CarGarage(models.Model):
    _name ='creditcalc.cargarage'

    name = fields.Char(compute='_concatinate_car_characteristics')
    # brand_ids = fields.One2many(comodel_name='creditcalc.carbrand', inverse_name='garage_id', string="Brand", required=True)
    # model_ids = fields.One2many(comodel_name='creditcalc.carmodel', inverse_name='garage_id', string="Model", ar_idrequired=True)
    # year_ids = fields.One2many(comodel_name='creditcalc.caryear', inverse_name='garage_id', string="Year", required=True)

    brand_id = fields.Many2one(comodel_name='creditcalc.carbrand', string="Brand", required=True)
    model_id = fields.Many2one(comodel_name='creditcalc.carmodel', string="Model", required=True)
    year_id = fields.Many2one(comodel_name='creditcalc.caryear', string="Year", required=True)

    kms = fields.Float(string="kms", required=True)
    price = fields.Float(string="Price", required=True)
    transmission = fields.Selection([
        ('1', "Manual"),
        ('2', "Automatic"),
        ('3', "Semi-automatic")
    ])
    color = fields.Char()
    owner_id = fields.Many2one('res.partner', ondelete='cascade', string="Owner", required=False)
    sold = fields.Boolean(default=False, readonly="True")

    @api.multi
    def _concatinate_car_characteristics(self):
        self.name = '{} {}, {} kms, {} UAH,'.format(
            self.brand_id.name, self.model_id.name, str(self.kms), str(self.price))


class CarBrand(models.Model):
    _name = 'creditcalc.carbrand'

    name = fields.Char(required=True)
    # garage_id = fields.Many2one(comodel_name='creditcalc.cargarage')

class CarModel(models.Model):
    _name = 'creditcalc.carmodel'

    name = fields.Char(required=True)
    # garage_id = fields.Many2one(comodel_name='creditcalc.cargarage')
    parent_id = fields.Many2one(comodel_name='creditcalc.carbrand')

class CarYear(models.Model):
    _name = 'creditcalc.caryear'

    name = fields.Integer(required=True)
    # garage_id = fields.Many2one(comodel_name='creditcalc.cargarage')
    parent_id = fields.Many2one(comodel_name='creditcalc.carmodel')

class Contract(models.Model):
    _name = 'creditcalc.contract'

    date = fields.Date(default=fields.Date.today)

    rate = fields.Float(string="Credit rate")

    term = fields.Selection([
        ('1', "1 month"),
        ('2', "2 months"),
        ('3', "3 months"),
        ('4', "4 months"),
        ('5', "5 months"),
        ('6', "6 months"),
        ('7', "7 months"),
        ('8', "8 months"),
        ('9', "9 months"),
        ('10', "10 months"),
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