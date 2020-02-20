
import os
from model import Library
import operator


def readline(file):
    return list(map(int, file.readline().strip().split()))

def read_file(file_path):
    with open(file_path) as file:
        n_books,  n_libraries,  days = readline(file)
        scores = readline(file)
        book_scores = {i: score for i, score in enumerate(scores)}
        libraries = []
        for i in range(n_libraries):
            _, signup_day, bpd = readline(file)
            books = {book: book_scores[book] for book in readline(file)}
            libraries.append(Library(i, books, signup_day, bpd))

        return {'book_scores': book_scores, 'days': days, 'libraries': libraries, 'n_books':n_books}


def solve_files(dir, solver):
    result_dir = os.path.join(dir, "..", "result")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    for file in os.listdir(dir):
        if not file.endswith('.txt'):
            continue
        print("Solving file :", file)
        inputs = read_file(os.path.join(dir, file))
        output = solver(inputs)
        with open(os.path.join(result_dir,file+'.sol'), "w") as solution:
            solution.write(str(len(output)) + "\n")
            for library in output:
                sorted_books = [k for k, v in sorted(library.books.items(), key=lambda item: item[1], reverse=True)]
                solution.write(str(library.id) + ' ' + str(len(library.books.items())) + "\n")
                solution.write(" ".join([str(i) for i in sorted_books]) + "\n")
