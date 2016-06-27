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

    term = fields.Selection(TERM_SELECTION, string="Term of credit")
    deposit = fields.Float(string="Deposit, UAH")

    car = fields.Many2one('creditcalc.cargarage')

    price = fields.Float(related='car.price', readonly="True")
    transmission = fields.Selection(related='car.transmission', readonly="True")
    color = fields.Char(related='car.color', readonly="True")


    # @api.multi
    # def _name_field_selection(self):
    #     for car in self.car:
    #         car.name

        # query = """
        # SELECT features
        # FROM table_option_twogitgit
        # WHERE name = 'something'
        # """
        # self.env.cr.execute(query)
        # return [(row[0], row[0]) for row in self.env.cr.fetchall()]
