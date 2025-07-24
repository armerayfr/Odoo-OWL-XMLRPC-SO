# -*- coding: utf-8 -*-

from odoo import models, fields, api
import uuid

class ResPartner(models.Model):
    _inherit = 'res.partner'

    external_token = fields.Char(string="External Token", readonly=True, index=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('external_token'):
                vals['external_token'] = str(uuid.uuid4())
        return super().create(vals_list)


class InvoiceRequest(models.Model):
    _name = 'invoice.request'
    _description = 'Invoice Request'

    partner_id = fields.Many2one(
        'res.partner',
        string="Customer"
    )
    sale_id = fields.Many2one(
        'sale.order',
        string="Sale Order Number",
        domain="[('state', '=', 'sale'), ('invoice_status', '=', 'to invoice'), ('partner_id', '=', partner_id)]",
        required=1
    )
    invoice_id = fields.Many2one(
        'account.move',
        string="Invoice Number"
    )
    status = fields.Selection(
        [
            ('pending', 'Pending'),
            ('approved', 'Approved')
        ],
        default='pending'
    )

    def approval_request(self):
        adv_payment_inv = self.env['sale.advance.payment.inv'].create(
            {
                'sale_order_ids': [(6, 0, self.sale_id.ids)]
            }
        )

        invoice_id = adv_payment_inv._create_invoices(adv_payment_inv.sale_order_ids)

        invoice_id.action_post()
        self.write(
            {
                'invoice_id': invoice_id.id,
                'status': 'approved'
            }
        )


