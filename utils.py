
import os
from model import Library

def readline(file):
    return list(map(int, file.readline().strip().split()))

def read_file(file_path):
    with open(file_path) as file:
        n_books,  n_libraries,  days = readline(file)
        scores = readline(file)
        book_scores = {i:score for i, score in enumerate(scores)}
        libraries = []
        for i in range(n_libraries):
            _, signup_day, bpd = readline(file)
            books = {book:book_scores[book] for book in readline(file)}
            libraries.append(Library(i, books, signup_day, bpd))
        return {'book_scores':book_scores, days:'days', 'libraries':libraries}

def solve_files(dir, solver):
    result_dir = os.path.join(dir,"..","result")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    for file in os.listdir(dir):
        if not file.endswith('.txt'):
            continue
        print("Solving file :",file)
        inputs = read_file(os.path.join(dir, file))
        output = solver(inputs)
        with open(os.path.join(result_dir,file+'.sol'), "w") as solution:
            pass
        #     for vehicle, rides in vehicle_rides.items():
        #         solution.write(str(vehicle) + ' ')
        #         solution.write(" ".join([str(i) for i in rides]) + "\n")
