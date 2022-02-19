from odoo import fields, models, api

class Collection(models.Model):
    _inherit = 'product.template'

    books = fields.Many2many('book', string="Books", store=True)
