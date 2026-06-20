import pytest
from main import BooksCollector

class TestBooksCollector:

# ========== добавляем новую книгу ==========
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

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

# ========== устанавливаем книге жанр ==========
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.get_book_genre('Книга') == ''

# ========== выводим список книг с определённым жанром ==========
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_valid(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', genre)
        result = collector.get_books_with_specific_genre(genre)
        assert 'Книга 1' in result

    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        result = collector.get_books_with_specific_genre('Роман')
        assert result == []

# ========== получаем жанр книги по её имени ==========
    def test_get_book_genre_book_exists_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_get_book_genre_book_exists_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        assert collector.get_book_genre('Книга') == ''

    def test_get_book_genre_book_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_case_sensitivity(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        assert collector.get_book_genre('книга') is None

 # ========== возвращаем книги, подходящие детям ==========
    def test_get_books_for_children_no_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Детская книга' in result

    def test_get_books_for_children_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Ужасная книга' not in result

    def test_get_books_for_children_mixed(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        collector.add_new_book('Детективная книга')
        collector.set_book_genre('Детективная книга', 'Детективы')
        result = collector.get_books_for_children()
        assert 'Детская книга' in result
        assert 'Ужасная книга' not in result
        assert 'Детективная книга' not in result

# ========== добавляем книгу в Избранное ==========
    def test_add_book_in_favorites_book_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

# ========== удаляем книгу из Избранного ==========
    def test_delete_book_from_favorites_book_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 1

 # ========== получаем список Избранных книг ==========
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга 1' in favorites
        assert 'Книга 2' in favorites