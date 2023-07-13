from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charges = fields.Float(string="Delivery Charges", store=True)

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            total_amount = amount_untaxed + amount_tax
            delivery_charge = total_amount * 0.1
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'delivery_charges': delivery_charge,
                'amount_total': total_amount + delivery_charge,
            })
