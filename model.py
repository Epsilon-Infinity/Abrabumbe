
class Library:

    def __init__(self, id, books, signup_days, book_p_day):
        self.id = id
        self.books = books
        self.signup_days = signup_days
        self.book_p_day = book_p_day

    def score(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])

        return possible_reward * self.book_p_day / self.signup_days

    def score2(self):
        pass
