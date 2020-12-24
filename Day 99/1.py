import sys
from math import sqrt
 
# Utility function to return the distance between two vertices in a 2-dimensional plane
def dist(x, y):
    # The distance between vertices `(x1, y1)` & `(x2, y2)` is
    # `√((x2 − x1) ^ 2 + (y2 − y1) ^ 2)`
    return sqrt((x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1]))
 
 
# Function to calculate the weight of optimal triangulation of a convex polygon
# represented by a given set of vertices
def MWT(vertices):
    # get the number of vertices in a polygon
    n = len(vertices)
 
    # create a table for storing the solutions to subproblems
    # `T[i][j]` stores the weight of the minimum-weight triangulation
    # of the polygon below edge `ij`
    T = [[0.0] * n for _ in range(n)]
 
    # fill the table diagonally using the recurrence relation
    for diagonal in range(n):
        i = 0
        for j in range(diagonal, n):
            # If the polygon has less than 3 vertices, triangulation is not possible
            if j >= i + 2:
                T[i][j] = sys.maxsize
                # consider all possible triangles `ikj` within the polygon
                for k in range(i + 1, j):
                    # The weight of a triangulation is the length its perimeter
                    weight = dist(vertices[i], vertices[j]) + \
                            dist(vertices[j], vertices[k]) + \
                            dist(vertices[k], vertices[i])
                    # choose the vertex `k` that leads to the minimum total weight
                    T[i][j] = min(T[i][j], weight + T[i][k] + T[k][j])
            i += 1
 
    # the top-rightmost element in the table stores the result
    return T[0][-1]
 
 

