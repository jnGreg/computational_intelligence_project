import matplotlib.pyplot as plt
import numpy as np


def cvrp_visulization_before(T):
    data = [el.location for el in T.points]
    data_in_array = np.array(data)
    transposed = data_in_array.T
    x, y = transposed

    plt.scatter(x, y)
    plt.scatter(x[0], y[0], color='gold', marker="X", s=750)
    plt.title("Rozmieszczenie punktów dostawy/odbioru oraz magazynu przed wyznaczeniem tras");
    plt.show()


def cvrp_visulization_after(T, routes):
    data = [el.location for el in T.points]
    coordinates_to_vis_all = []
    for route in routes:
        coordinates_to_vis = []
        for point in route:
            coordinates_to_vis.append(data[point])
        coordinates_to_vis_all.append(coordinates_to_vis)


    route_colors = ['green', 'yellow', 'blue', 'grey', 'red', 'orange', 'brown']
    for index, route in enumerate(coordinates_to_vis_all):
        data_in_array = np.array(route)
        transposed = data_in_array.T
        x, y = transposed
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.scatter(x[0], y[0], color=route_colors[index])


    plt.scatter(x[0], y[0], color='gold', marker="X", s=750)
    plt.title("Rozmieszczenie punktów dostawy/odbioru oraz magazynu po wyznaczeniu tras");
    plt.show()