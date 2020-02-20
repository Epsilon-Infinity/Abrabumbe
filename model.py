class Library:

    def __init__(self, id, books, signup_days, book_p_day):
        self.id = id
        self.books = books
        self.signup_days = signup_days
        self.book_p_day = book_p_day

    def score(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])

        return possible_reward * self.book_p_day / self.signup_days

    def score2(self, books_so_far, days_left):
        books = sorted(self.books.items(), key=lambda x: x[1], reverse=True)
        n_books = int(days_left / self.book_p_day)
        selected = []
        i = 0
        while n_books > 0 and i < len(books):
            if books[i][0] not in books_so_far:
                selected.append(books[i][1])
                n_books -= 1
            i += 1

        return sum(selected) * self.book_p_day / self.signup_days

    def score2(self):
        pass
