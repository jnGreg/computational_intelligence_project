
# from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task
from functions.load_truck import load_truck
from functions.unload_truck import unload_truck

def main():
    points=generate_task().points
    cars=generate_task().trucks

    point=points[0]
    car=cars[0]

    print('init')
    print(point)
    print(car)

    print('ŁADUJEMY')
    car,point = load_truck(car,point)
    print(point)
    print(car)

    print('UNŁADUJEMY')
    car,point = unload_truck(car,point)

    print(point)
    print(car)


if __name__ == "__main__":
    main()
