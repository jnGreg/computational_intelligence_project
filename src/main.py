import random

from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task
from functions.drive_truck import drive_truck
from functions.load_truck import load_truck
from functions.unload_truck import unload_truck
from functions.vrp_solution import cvrp
from functions.visualization import cvrp_visulization_before,cvrp_visulization_after
import pandas as pd


def main():
    T = generate_task(400,600)
    df = generate_dist_matrix(T.points)
    print("Task initiation info")
    print("Number of points", len(T.points)+1)
    print("Number of trucks", len(T.trucks)+1)
    print("Truck specyfication")
    for t in T.trucks:
        print(t)

    print('CVRP solution ')
    routes=cvrp(T)
    cvrp_visulization_before(T)
    cvrp_visulization_after(T, routes)



if __name__ == "__main__":
    main()
