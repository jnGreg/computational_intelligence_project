import pandas as pd
from scipy.spatial import distance

import math


def calc_euc_dist(p1, p2):
    """
    function to calculate the distance between two coordinate points
    p1 - point object
    p2 - point object
     :return distance: distance beetwen two points od coordintes
     """
    point_1 = p1[0:2]
    point_2 = p2[0:2]
    dist = math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)
    return dist


def generate_dist_matrix(list_of_points):
    """
    function for generating distance matrices from coordinates of points
    list_of_points: list of objects (Point)
         :return df_mat_dis: dataframe with distance matrix
         """
    cords = []
    n = 0
    for p in list_of_points:
        cords.append(p[0:2])
        n += 1
    mat_dist = distance.cdist(cords, cords, 'euclidean')
    df_mat_dist = pd.DataFrame(mat_dist)
    return df_mat_dist

# test
# T = generate_task()
# B = generate_dist_matrix(T.points)
# print(B)
