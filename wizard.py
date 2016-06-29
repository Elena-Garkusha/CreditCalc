# -*- coding: utf-8 -*-

from openerp import models, fields, api

TERM_SELECTION = [
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
]

class Wizard(models.TransientModel):
    _name = 'creditcalc.wizard'


    brand = fields.Many2one('creditcalc.carbrand', string="Brand")
    model = fields.Many2one('creditcalc.carmodel', string="Model")
    year = fields.Many2one('creditcalc.caryear', string="Year")
    date = fields.Date(default=fields.Date.today)
    term = fields.Selection(TERM_SELECTION, string="Term of credit")
    deposit = fields.Float(string="Deposit, UAH")

    car = fields.Many2one('creditcalc.cargarage')
    car_price = fields.Float(related='car.price', readonly="True")
    transmission = fields.Selection(related='car.transmission', readonly="True")
    color = fields.Char(related='car.color', readonly="True")

    discount =fields.Float(compute='_sum_of_discount')
    sum = fields.Float(compute='_sum_of_credit', string="Credit sum")
    rate = fields.Float(compute='_change_credit_rate', string="Credit rate", readonly="True")

    @api.depends('deposit', 'car_price')
    def _sum_of_discount(self):
        for r in self:
            if r.deposit >= r.car_price*0.8:
                r.discount = r.car_price*0.12
            elif r.deposit >= r.car_price*0.78:
                r.discount = r.car_price*0.09
            elif r.deposit >= r.car_price*0.76:
                r.discount = r.car_price*0.07
            elif r.deposit >= r.car_price*0.75:
                r.discount = r.car_price*0.05
            else: r.discount = 0

    @api.depends('car_price', 'deposit', 'discount')
    def _sum_of_credit(self):
        for r in self:
            r.sum = r.car_price - r.deposit - r.discount

    @api.one
    @api.onchange('term')
    def _change_credit_rate(self):
        base_rate = self.env['creditcalc.rate'].search([('date', '=', self.date)])
        if int(self.term) <= 3:
            self.rate = base_rate.name
        else:
            self.rate = base_rate.name + float(self.term)/3.0