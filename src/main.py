import random

from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task
from functions.drive_truck import drive_truck
from functions.load_truck import load_truck
from functions.unload_truck import unload_truck
from functions.vrp_solution import cvrp
import pandas as pd


def main():
    T = generate_task(400,600)
    df = generate_dist_matrix(T.points)
    print("Task initiation info")
    print("Number of points", len(T.points)+1)
    print("Number of trucks", len(T.trucks))
    print("Truck specification")
    for t in T.trucks:
        print(t)



    print('CVRP solution ')
    cvrp(T)





if __name__ == "__main__":
    main()
