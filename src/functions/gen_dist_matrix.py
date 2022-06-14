import pandas as pd
from scipy.spatial import distance
from src.classes.point import Point
from src.classes.transport_task import TransportTask
import math


def calc_euc_dist(p1: Point, p2: Point):
    """
    function to calculate the distance between two coordinate points
    p1 - point object
    p2 - point object
     :return distance: distance beetwen two points od coordintes
     """
    point_1 = p1.location
    point_2 = p2.location
    dist = math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)
    return dist


def generate_dist_matrix(list_of_points: TransportTask.points):
    """
    function for generating distance matrices from coordinates of points
    list_of_points: list of objects (Point)
         :return df_mat_dis: dataframe with distance matrix
         """
    cords = []
    n = 0
    for p in list_of_points:
        cords.append(p.location)
        n += 1
    mat_dist = distance.cdist(cords, cords, 'euclidean')
    df_mat_dist = pd.DataFrame(mat_dist)
    return df_mat_dist

# test
# T = generate_task()
# B = generate_dist_matrix(T.points)
# print(B)
