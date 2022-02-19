from odoo.tests.common import TransactionCase
from psycopg2 import IntegrityError
from psycopg2.errors import CheckViolation
from odoo.tools import mute_logger
import datetime

import logging

_logger = logging.getLogger(__name__)

class TestBook(TransactionCase):

    def test_create(self):
        "Create a simple book"
        Book = self.env['book']
        book = Book.create({
            'name': 'Harry Potter', 
            'description': 'Un livre Harry Potter', 
            'publication_date': '2020-12-12',
            'pages_count': 300,
            })
        self.assertEqual(book.name, 'Harry Potter')
        self.assertEqual(book.description, 'Un livre Harry Potter')
        self.assertEqual(book.publication_date, datetime.date(2020, 12, 12))
        self.assertEqual(book.pages_count, 300)

    def test_create_non_unique_name(self):
        "Create a book with a non unique name"
        Book = self.env['book']
        book = Book.create({
            'name': 'Harry Potter',
            'description': 'Un livre Harry Potter',
            'publication_date': '2020-12-12',
            'pages_count': 300,
        })
        with self.assertRaises(IntegrityError):
            with mute_logger('odoo.sql_db'):
                book = Book.create({
                    'name': 'Harry Potter', 
                    'description': 'Un livre Harry Potter', 
                    'publication_date': '2020-12-12',
                    'pages_count': 300,
                    })

    def test_create_date_exception(self):
        "Create a book with bad publication date"
        Book = self.env['book']
        with self.assertRaises(IntegrityError):
            with mute_logger('odoo.sql_db'):
                book = Book.create({
                    'name': 'Harry Potter', 
                    'description': 'Un livre Harry Potter', 
                    'publication_date': '2025-12-12',
                    'pages_count': 300,
                    })

    def test_create_pages_count_exception(self):
        "Create a book with 0 pages"
        Book = self.env['book']
        with self.assertRaises(IntegrityError):
            with mute_logger('odoo.sql_db'):
                book = Book.create({
                    'name': 'Harry Potter',
                    'description': 'Un livre Harry Potter',
                    'publication_date': '1999-06-15',
                    'pages_count': 0,
                })
