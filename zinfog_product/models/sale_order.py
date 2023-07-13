from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand_name = fields.Char(string="Brand Name", related='product_id.brand_name')
