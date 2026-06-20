import pytest
from main import BooksCollector

class TestBooksCollector:

# ========== добавляем новую книгу ==========
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

def test_add_new_book_name_more_than_40_symbols(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name', ['Книга 1', 'Книга 2', 'Книга с названием'])
    def test_add_new_book_different_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        assert collector.get_book_genre(name) == ''

    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

