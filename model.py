class Library:

    def __init__(self, id, books, signup_days, book_p_day):
        self.id = id
        self.books = books
        self.signup_days = signup_days
        self.book_p_day = book_p_day

    def score(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])
        return possible_reward * self.book_p_day / self.signup_days
    
    def score4(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])
        return possible_reward * self.book_p_day / self.signup_days**3

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

    def score3(self, books_so_far):
        possible_reward = sum([self.books[id] for id in self.books.keys() if id not in books_so_far])
        return possible_reward * self.book_p_day / self.signup_days**6

    def score5(self, books_so_far):
        scores = [self.books[id] for id in self.books.keys() if id not in books_so_far]
        possible_reward = sum(scores)
        return 0 if len(scores)==0 else possible_reward * (len(scores) - self.signup_days) / len(scores)

