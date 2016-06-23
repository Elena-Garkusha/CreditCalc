# -*- coding: utf-8 -*-

from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    car_ids = fields.One2many('creditcalc.car', 'owner_id', string="Car")
    # contract_ids = fields.One2many()