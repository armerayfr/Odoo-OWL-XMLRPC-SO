from infrastructure.odoo_xmlrpc import OdooXMLRPCClient

class SaleOrderService:
    def __init__(self, client: OdooXMLRPCClient):
        self.client = client

    def create(self, partner_id, order_lines):
        lines = [(0, 0, {
            'product_id': l['product_id'],
            'product_uom_qty': l['quantity']
        }) for l in order_lines]

        return self.client.call('sale.order', 'create', [{
            'partner_id': partner_id,
            'order_line': lines
        }])

    def read(self, so_id):
        return self.client.call('sale.order', 'read', [[so_id]])

    def search(self):
        return self.client.call('sale.order', 'search_read', [[]])

    def write(self, so_id, updates):
        return self.client.call('sale.order', 'write', [[so_id], updates])

    def confirm(self, so_id):
        return self.client.call('sale.order', 'action_confirm', [[so_id]])

    def cancel(self, so_id):
        return self.client.call('sale.order', 'action_cancel', [[so_id]], kwargs={
            'context': {
                'disable_cancel_warning': True
            }
        })

    def reset_draft(self, so_id):
        return self.client.call('sale.order', 'action_draft', [[so_id]])

    def update(self, so_id, updates: dict):
        return self.client.call(
            'sale.order',
            'write',
            [[so_id], updates]
        )

