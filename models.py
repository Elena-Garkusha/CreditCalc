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

class CarGarage(models.Model):
    _name ='creditcalc.cargarage'

    name = fields.Char(compute='_concatinate_car_characteristics')
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

class CarModel(models.Model):
    _name = 'creditcalc.carmodel'

    name = fields.Char(required=True)
    parent_id = fields.Many2one(comodel_name='creditcalc.carbrand')

class CarYear(models.Model):
    _name = 'creditcalc.caryear'

    name = fields.Integer(required=True)
    parent_id = fields.Many2one(comodel_name='creditcalc.carmodel')

class Contract(models.Model):
    _name = 'creditcalc.contract'

    date = fields.Date(default=fields.Date.today)
    # date_for_rate = fields.Many2one(comodel_name='creditcalc.rate', compute='_date_for_rate')
    # date_for_rate2 = fields.Date(compute='_date_for_rate')
    # base_rate = fields.Float(related='date_for_rate2.rate')
    # base_rate = fields.Float(compute='date_for_rate.rate');
    rate = fields.Float(compute='_change_credit_rate', string="Credit rate", readonly="True")
    # rate = fields.Float()
    term = fields.Selection(TERM_SELECTION, string="Term of contract", required=True)

    customer_id = fields.Many2one('res.partner', ondelete='cascade', string="Customer")
    brand = fields.Many2one('creditcalc.carbrand', string="Brand")
    model = fields.Many2one('creditcalc.carmodel', string="Model")
    year = fields.Many2one('creditcalc.caryear', string="Year")
    car = fields.Many2one(comodel_name='creditcalc.cargarage')
    car_price = fields.Float(related='car.price', readonly="True")
    transmission = fields.Selection(related='car.transmission', readonly="True")
    color = fields.Char(related='car.color', readonly="True")

    deposit = fields.Float(string="Deposit", required=True)
    discount = fields.Float(compute='_sum_of_discount')

    sum = fields.Float(compute='_sum_of_contract', string="Sum of contract")
    state = fields.Selection([
        ('new', "New"),
        ('signed', "Signed"),
        ('expired', "Expired"),
        ('canceled', 'Canceled'),
    ],string="State of contract", default="new")

    # @api.multi
    # @api.depends('date')
    # def _date_for_rate(self):
    #     pass
    #     # print "################" + "********************"
    #     # self._date_for_rate = self.date
    #     # for r in self:
    #         # for d in self.date_for_rate:
    #         # print "################" + str(r.date_for_rate)+ "##################"
    #             # print "**************" + str(d)+ "************"
    #             # if d.date == self.date:
    #             #     self.date_for_rate = d.date

    @api.onchange('term')
    def _change_credit_rate(self):
        base_rate = self.env['creditcalc.rate'].search([('date', '=', self.date)])
        # print "******************" + str(base_rate)
        # self.rate = base_rate.name
        for r in self:
            if int(self.term) <= 3:
                self.rate = base_rate.name
            else:
                self.rate = base_rate.name + float(self.term)/3.0

    @api.depends('deposit', 'car_price')
    def _sum_of_discount(self):
        for r in self:
            if r.deposit >= r.car_price*0.75:
                r.discount = r.car_price*0.05
            else: r.discount = 0

    @api.depends('car_price', 'deposit', 'discount')
    def _sum_of_contract(self):
        for r in self:
            r.sum = r.car_price - r.deposit - r.discount

class BaseRate(models.Model):
    _name = 'creditcalc.rate'

    date = fields.Date(default=fields.Date.today)
    name = fields.Float(required=True, string="Credit rate")