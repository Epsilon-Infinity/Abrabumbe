
class Library:

    def __init__(self, books, signup_days, book_p_day):
        self.books = books
        self.signup_days = signup_days
        self.book_p_day = book_p_day

    def score(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])

    def score2(self):
        pass
