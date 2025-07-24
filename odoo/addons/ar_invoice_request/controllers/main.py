from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class ExternalInvoiceController(http.Controller):

    @http.route(['/external/sale-invoice/<string:token>'], type='http', auth='public', website=True)
    def external_invoice_page(self, token, **kwargs):
        _logger.info("========TOKEN================")
        _logger.info(token)
        return request.render('ar_invoice_request.external_template_wrapper', {
            'token': token
        })

    @http.route(['/external/api/sale-info/<string:token>'], type='json', auth='public')
    def get_sale_orders(self, token, **kwargs):
        partner = request.env['res.partner'].sudo().search([('external_token', '=', token)], limit=1)
        sale_orders = request.env['sale.order'].sudo().search([
            ('partner_id', '=', partner.id),
            ('state', '=', 'sale'),
            ('invoice_status', '=', 'to invoice')
        ])
        return {
            'partner': {'id': partner.id, 'name': partner.name},
            'orders': [{'id': so.id, 'name': so.name} for so in sale_orders],
            'invoice_url': None  # Diisi kalau sudah ada invoice
        }

    @http.route(['/external/api/request-invoice'], type='json', auth='public', methods=['POST'])
    def request_invoice(self, **post):
        token = post.get('token')
        so_id = post.get('sale_order_id')
        partner = request.env['res.partner'].sudo().search([('external_token', '=', token)], limit=1)
        request.env['invoice.request'].sudo().create({
            'partner_id': partner.id,
            'sale_id': so_id,
            'status': 'pending',
        })
        return {'status': 'ok'}
