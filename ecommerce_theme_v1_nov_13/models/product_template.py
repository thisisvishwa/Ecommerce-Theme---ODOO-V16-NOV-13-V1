```python
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gpu_type = fields.Char(string='GPU Type')
    ram_size = fields.Integer(string='RAM Size')
    product_type = fields.Selection([
        ('pc', 'Gaming PC'),
        ('laptop', 'Gaming Laptop'),
        ('component', 'PC Component'),
        ('console', 'Gaming Console'),
        ('other', 'Other')
    ], string='Product Type', default='other')

    def get_product_specs(self):
        specs = super(ProductTemplate, self).get_product_specs()
        specs.update({
            'gpu_type': self.gpu_type,
            'ram_size': self.ram_size,
            'product_type': self.product_type,
        })
        return specs
```