# -*- coding: utf-8 -*-

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    delivery_pricelist_id = fields.Many2one(
        'product.pricelist',
        string="Sale Pricelist",
        domain=[('type','=','sale')])

