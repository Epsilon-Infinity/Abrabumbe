import utils
from copy import deepcopy
from collections import defaultdict

def solver(inputs):
    rides_list = inputs['rides_list']
    rides_list = sorted([Ride(ride_info, i) for i, ride_info in  enumerate(rides_list)])
    sol = defaultdict(list)
    vehicles = [Vehicle(i+1, inputs['bonus']) for i in range(inputs['vehicles'])]
    for ride in rides_list:
        best, vehicle = None, None
        for v in vehicles:
            cur = v.score_if_assigned(ride)
            if (not vehicle) or (cur[0] > best[0] or cur[0] == best[0] and cur[1] < best[1]):
                best, vehicle = cur, v
        vehicle.assign(ride)
    sol = {v.id:v.get_idx() for v in vehicles}
    return sol

if __name__=="__main__":
    utils.solve_files('data', solver)