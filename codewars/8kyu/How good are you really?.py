from numpy import mean


def better_than_average(class_points, your_points):
    return True if mean(class_points) < your_points else False
