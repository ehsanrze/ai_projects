class Node:
    def __init__(self, coordinate, cost, f_n, parent):
        self.coordinate = coordinate
        self.path_cost = cost
        self.f_n = f_n
        self.parent = parent
