# -*- coding: utf-8 -*-

from openerp import models, fields, api

class online_store(models.Model):
    _name = 'online_store.products'

    name = fields.Char(string="Product")
    category = fields.Char()
    price = fields.Float()
    amount = fields.Integer()
    seller = fields.Char()