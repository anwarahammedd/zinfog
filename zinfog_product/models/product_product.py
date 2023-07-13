from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    minimum_cost = fields.Float(string='Minimum Cost')
    brand_name = fields.Char(string="Brand Name")

    @api.constrains('minimum_cost')
    def _check_minimum_cost(self):
        if self.minimum_cost > self.lst_price:
            raise ValidationError("The unit price should not be less than the minimum cost.")
