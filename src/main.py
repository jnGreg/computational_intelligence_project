from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task
from functions.load_truck import load_truck
from functions.unload_truck import unload_truck
from functions.vrp_solution import vrp
def main():
    T = generate_task(100,500)
    print(generate_dist_matrix(T.points))
    # # print(generate_dist_matrix(T.points))
    ## Car logic test
    points = T.points
    cars = T.trucks

    point = points[0]
    car = cars[0]

    print('init')
    print(point)
    print(car)

    print('Load truck')
    car, point = load_truck(car, point)
    print(point)
    print(car)

    print('Unload truck')
    car, point = unload_truck(car, point)

    print(point)
    print(car)

    #### VRP solution
    print('VRP')
    vrp()


if __name__ == "__main__":
    main()
