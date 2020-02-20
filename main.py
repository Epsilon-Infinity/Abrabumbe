import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    book_scores = inputs["book_scores"]
    deadline = inputs["days"]
    libraries = inputs["libraries"]
    result = []
    while  len(libraries)>0:
        libraries = sorted(libraries, key=lambda x: x.score(books_so_far))
        result.append(libraries[0])
        for book in libraries[0].books.keys():
            books_so_far.add(book)
        libraries.pop(0)

    return result


if __name__ == "__main__":
    utils.solve_files('data', solver)
