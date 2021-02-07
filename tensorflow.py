import tensorflow as tf
import timeit
import numpy as np

def compute_error_for_line_given_point(b_gradient,w_current,points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i,0]
        y = points[i,1]

        b_gradient += (2/n) * ((w_current * x +b_current)- y)
