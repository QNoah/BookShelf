import unittest
from ..book import Book

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.book_null = Book(title=None)

    def test_book_is_null(self):
        self.assertIsNone(self.book_null.title)