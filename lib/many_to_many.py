# lib/book.py
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)


# lib/author.py
class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []  # Keeps track of contracts
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


# lib/contract.py
class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
