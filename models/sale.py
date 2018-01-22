# -*- coding: utf-8 -*-

from openerp import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def onchange_delivery_id(self, cr, uid, ids, company_id, partner_id,
        delivery_id, fiscal_position, context=None):
        res = super(SaleOrder, self).onchange_delivery_id(
            cr, uid, ids, company_id, partner_id,
            delivery_id, fiscal_position, context=context)
        if delivery_id:
            partner = self.pool.get('res.partner').browse(
                cr, uid, delivery_id, context=context)
            if partner.delivery_pricelist_id:
                res['value']['pricelist_id'] =\
                    partner.delivery_pricelist_id.id
        return res

    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        res = super(SaleOrder, self).onchange_partner_id(
            cr, uid, ids, part, context=context)
        if part:
            addr = self.pool.get('res.partner').address_get(
                cr, uid, [part], ['delivery', 'invoice', 'contact'])
            delivery_onchange = self.onchange_delivery_id(
                cr, uid, ids, False, part,
                addr['delivery'], False,  context=context)
            if res and res['value']:
                res['value'].update(delivery_onchange['value'])
        return res
