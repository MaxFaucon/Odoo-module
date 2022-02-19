# -*- coding: utf-8 -*-
{
    'name': "lecture",

    'summary': """
        Module de vente de livres
    """,

    'description': """
        blabla
    """,

    'author': "52977-54456",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_view.xml',
        'views/lecture_menu.xml',
        'views/author_view.xml',
        'views/books_collection_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/books_demo.xml',
        'demo/products_demo.xml',
        'demo/stock_demo.xml',
    ],
    'application': 'true'
}
