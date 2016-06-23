# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'creditcalc.wizard'

    name = fields.Many2one(comodel_name='creditcalc.car', String="Brand")
    model = fields.Many2one('creditcalc.car', String="Model")
    year = fields.Many2one('creditcalc.car', String="Year")

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
    ],String="Term of credit")
    deposit = fields.Float(String="Deposit, UAH")
    #
    # discount = field.
    # rate =
    # payment =
    # price=

    # def _default_sessions(self):
    #     return self.env['openacademy.session'].browse(self._context.get('active_ids'))
    #
    # session_ids = fields.Many2many('openacademy.session',
    #     string="Sessions", required=True, default=_default_sessions)
    # attendee_ids = fields.Many2many('res.partner', string="Attendees")
    #
    # @api.multi
    # def subscribe(self):
    #     for session in self.session_ids:
    #         session.attendee_ids |= self.attendee_ids
        # return {}