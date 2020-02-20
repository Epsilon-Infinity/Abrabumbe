
import os


def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        rows, columns, vehicles, rides, bonus, steps = list(map(int, lines[0].strip().split()))
        rides_list = [list(map(int, line.strip().split())) for line in lines[1:] ]
        return {'rows':rows, columns:'columns', 'vehicles':vehicles,\
             'rides':rides, 'bonus':bonus, 'steps':steps, 'rides_list':rides_list}

def solve_files(dir, solver):
    result_dir = os.path.join(dir,"..","result")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    for file in os.listdir(dir):
        if not file.endswith('.in'):
            continue
        print("Solving file :",file)
        inputs = read_file(os.path.join(dir, file))
        vehicle_rides = solver(inputs)
        with open(os.path.join(result_dir,file+'.sol'), "w") as solution:
            for vehicle, rides in vehicle_rides.items():
                solution.write(str(vehicle) + ' ')
                solution.write(" ".join([str(i) for i in rides]) + "\n")
