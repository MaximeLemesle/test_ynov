import pytest # type: ignore
from src.bibliotheque.book import Book

class TestBookCreation:
    """Tests de création de livre"""
    def test_create_valid_book(self):
        book = Book("Titre", "Auteur", "1234567890123")
        assert book.title == "Titre"
        assert book.author == "Auteur"
        assert book.isbn == "1234567890123"
        assert book.is_available() is True

    def test_create_book_empty_title_raises_error(self):
        with pytest.raises(ValueError, match="titre"):
            Book("", "Auteur", "1234567890123")

    def test_create_book_invalid_isbn_raises_error(self):
        with pytest.raises(ValueError, match="ISBN"):
            Book("Titre", "Auteur", "12345678901")  # 12 caractères
        with pytest.raises(ValueError, match="ISBN"):
            Book("Titre", "Auteur", "12345678901234")  # 14 caractères

class TestBookBorrowing:
    """Tests d'emprunt de livre"""
    def setup_method(self):
        self.book = Book("Titre", "Auteur", "1234567890123")

    def test_new_book_is_available(self):
        assert self.book.is_available() is True

    def test_borrow_available_book_success(self):
        result = self.book.borrow()
        assert result is True
        assert self.book.is_available() is False

    def test_borrow_already_borrowed_book_fails(self):
        self.book.borrow()
        result = self.book.borrow()
        assert result is False

    def test_return_book_not_borrowed_fails(self):
        result = self.book.return_book()
        assert result is False

    def test_return_borrowed_book_success(self):
        self.book.borrow()
        result = self.book.return_book()
        assert result is True
        assert self.book.is_available() is True 