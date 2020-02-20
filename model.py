
class Library:

    def __init__(self, books, signup_days, book_p_day):
        self.books = books
        self.signup_days = signup_days
        self.book_p_day = book_p_day

    def score(self):
        return (sum(self.books.values()) + self.book_p_day) / self.signup_days

    def score2(self):
        pass
        