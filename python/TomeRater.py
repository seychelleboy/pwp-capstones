import re

class User(object):
    def __init__(self, name, email):
        self.name = name ## set name as string
        self.email = email ## set email as string
        self.books = {} ##creating empty dictionary

    def get_email(self):
        return self

    def change_email(self, new_email):
        self.email = new_email ## set address
        print("Your email address has been updated successfully.") ##return msg once email updated

    def __repr__(self):
        return "User - {name}, Email: {email}, Books you've read: {books_read}".format(name = self.name, email = self.email, books_read = str(len(self.books)))


    def __eq__(self, check_other_user):
        if self.name == check_other_user:
            return True
        else:
            return False


    def read_book(self, book, rating = None):
        self.books[book] = rating


    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.books.values():
            ratings_total += rating
        average_rating = ratings_total / len(self.books)
        return average_rating



class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
       return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
	
#work out average rating
    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.ratings:
            ratings_total += rating
        average_rating = ratings_total / len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_isbn):
        if self.isbn == other_isbn:
            return True
        else:
            return False

    def __repr__(self):
        return "{title}, ISBN: {isbn}".format(title = self.title, isbn = self.isbn)
####################################


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)



class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)



class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        ##email validation
        valid = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        check = email
        match = re.match(valid, check)
        if match != None:
            self.users[email] = new_user
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("Invalid email format {}".format(email))		

    def print_catalog(self):
        for title in self.books.keys():
            print(title)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        most_read = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                read_count = self.books[book]
            if self.books[book] == read_count:
                most_read = book
        return most_read

    def highest_rated_book(self):
        highest_book = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_book = book
        return highest_book

    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_user = user
        return highest_user
