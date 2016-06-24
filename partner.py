# -*- coding: utf-8 -*-

from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # name = fields.Char(required=True)
    car_ids = fields.One2many('creditcalc.cargarage', 'owner_id', string="Car")
    # contract_ids = fields.One2many()