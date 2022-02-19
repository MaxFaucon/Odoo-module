from odoo import models, fields, api


class Book(models.Model):
    _name = 'book'
    _description = 'Book'

    name = fields.Char(required=True)
    description = fields.Char()
    cover_image = fields.Binary('Image')
    publication_date = fields.Date(required=True)
    pages_count = fields.Integer()
    authors = fields.Many2many('res.partner', string="Authors")
    like_ids = fields.Many2many('res.users', string="Likes")

    has_authors = fields.Integer(compute="_compute_has_authors", store=True)
    like_count = fields.Integer(compute="_compute_likes", store=True)
    user_has_liked = fields.Char(compute="_compute_user_has_liked")

    @api.depends('authors')
    def _compute_has_authors(self):
        for record in self:
            record.has_authors = len(record.authors) > 0

    @api.depends('like_ids')
    def _compute_likes(self):
        for record in self:
            record.like_count = len(record.like_ids)

    @api.depends('like_ids')
    def _compute_user_has_liked(self):
        current_user_like = self.search([('like_ids', 'in', [self.env.user.id]), ('id', '=', self.id)])

        if current_user_like:
            self.user_has_liked = "Vous avez aimé"
        else:
            self.user_has_liked = ""
    
    def action_like(self):
        current_user_like = self.search([('like_ids', 'in', [self.env.user.id]), ('id', '=', self.id)])

        if current_user_like:
            self.write({'like_ids': [(3, self.env.user.id)]})
        else:
            self.write({'like_ids': [(4, self.env.user.id)]})

    _sql_constraints = [
        (
            'book_name_unique',
            'UNIQUE(name)',
            'Book name must be unique',
        ),
        (
            'pages_counts_greater_than_0',
            'CHECK(pages_count > 0)',
            'The number of pages must be greater than 0',
        ),
        (
            'publication_date_before_today',
            'CHECK(publication_date < CURRENT_DATE)',
            'The publication date must be before current date',
        ),
    ]
