from odoo import fields, models, api

class Author(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string="Author", default=False)
    books = fields.Many2many('book', string="Books")
    books_count = fields.Integer(compute="_compute_books_count", store=True)

    @api.depends('books')
    def _compute_books_count(self):
        for record in self:
            record.books_count = len(record.books) 
