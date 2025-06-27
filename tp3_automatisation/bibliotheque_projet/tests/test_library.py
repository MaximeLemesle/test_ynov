import pytest # type: ignore
from src.bibliotheque.library import Library
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

class TestLibraryOperations:
    def setup_method(self):
        """Fixture complexe : bibliothèque avec livres et utilisateurs"""
        self.library = Library("Médiathèque")
        self.book1 = Book("Livre 1", "Auteur 1", "1111111111111")
        self.book2 = Book("Livre 2", "Auteur 2", "2222222222222")
        self.book3 = Book("Livre 3", "Auteur 3", "3333333333333")
        self.user1 = User("Alice", "alice@email.com")
        self.user2 = User("Bob", "bob@email.com")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_borrow_flow_success(self):
        """Test flux complet d'emprunt réussi"""
        result = self.library.borrow_book(self.user1, "1111111111111")
        assert result is True
        assert self.book1.is_available() is False
        assert self.book1 in self.user1.borrowed_books

    def test_user_cannot_borrow_more_than_limit(self):
        """Test limite d'emprunts par utilisateur"""
        self.library.borrow_book(self.user1, "1111111111111")
        self.library.borrow_book(self.user1, "2222222222222")
        self.library.borrow_book(self.user1, "3333333333333")
        # Tente un 4ème emprunt (doit échouer)
        book4 = Book("Livre 4", "Auteur 4", "4444444444444")
        self.library.add_book(book4)
        result = self.library.borrow_book(self.user1, "4444444444444")
        assert result is False
        assert book4.is_available() is True

    def test_borrow_inexistant_book_fails(self):
        """Test emprunt d'un livre inexistant"""
        result = self.library.borrow_book(self.user1, "9999999999999")
        assert result is False

    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt d'un livre déjà emprunté"""
        self.library.borrow_book(self.user1, "1111111111111")
        result = self.library.borrow_book(self.user2, "1111111111111")
        assert result is False

    def test_borrow_when_user_cannot_borrow(self):
        """Test emprunt refusé si l'utilisateur a atteint la limite"""
        self.library.borrow_book(self.user1, "1111111111111")
        self.library.borrow_book(self.user1, "2222222222222")
        self.library.borrow_book(self.user1, "3333333333333")
        # user1 ne peut plus emprunter
        result = self.library.borrow_book(self.user1, "1111111111111")
        assert result is False 