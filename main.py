import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    book_scores = inputs["book_scores"]
    days_left = inputs["days"]
    libraries = inputs["libraries"]
    result = []

    while  len(libraries)>0:
        libraries = sorted(libraries, key=lambda x: x.score2(books_so_far), reverse=True)
        result.append(libraries[0])
        for book in libraries[0].books.keys():
            books_so_far.add(book)
        libraries.pop(0)
        days_left -= result[-1].signup_days
        if len(result)%100==0:
            print(" of libraries selected ", len(result))

    return result


if __name__ == "__main__":
    utils.solve_files('data', solver)
