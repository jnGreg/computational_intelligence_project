from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task
from functions.drive_truck import drive_truck
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
    routes = vrp()

    # Display the routes.
    time_for_all_trucks = 0
    for i, route in enumerate(routes):
        print('Route', i, route)
        car = cars[int(i)]
        print("Status pojazdu przed trasą", car)
        for p in route:
            if points[p].cargo_amount > 0:
                car, point = unload_truck(car, points[p])
                #car = drive_truck(car.location, points[p].location) to jeszcze nie działa]
                time_for_all_trucks += car.total_time
            else:
                car, point =load_truck(car, points[p])
                time_for_all_trucks += car.total_time
        print("Status pojazdu po trasie", car)
        print("czas całkowity", time_for_all_trucks, " sekund")





if __name__ == "__main__":
    main()
