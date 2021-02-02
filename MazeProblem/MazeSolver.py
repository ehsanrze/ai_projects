from Node import Node


class Maze:

    def __init__(self, maze_rows, maze_cols, path, start, goal):
        self.heuristics = {}
        self.adjacency_list = {}
        self.maze_rows = maze_rows
        self.maze_cols = maze_cols

        self.path = path

        self.start = start
        self.goal = goal

        self.make_adjacency()
        self.make_heuristics()

    def make_adjacency(self):
        for i in range(0, self.maze_rows):
            for j in range(0, self.maze_cols):
                # list of current node adjacency
                node_adjacency = []
                if self.path[i][j] == 0:
                    # check if connect to top
                    if i - 1 >= 0:
                        if self.path[i - 1][j] == 0:
                            node_adjacency.append(str(i - 1) + " " + str(j))
                    # check if connect to left
                    if j - 1 >= 0:
                        if self.path[i][j - 1] == 0:
                            node_adjacency.append(str(i) + " " + str(j - 1))
                    # check if connect to right
                    if j + 1 < self.maze_cols:
                        if self.path[i][j + 1] == 0:
                            node_adjacency.append(str(i) + " " + str(j + 1))
                    # check if connect to down
                    if i + 1 < self.maze_rows:
                        if self.path[i + 1][j] == 0:
                            node_adjacency.append(str(i + 1) + " " + str(j))
                    self.adjacency_list[str(i) + " " + str(j)] = node_adjacency

    def make_heuristics(self):
        x, y = self.goal.split(" ")
        for i in range(0, self.maze_rows):
            for j in range(0, self.maze_cols):
                # calculate manhattan distance
                val = (int(x) - i) + (int(y) - j)
                self.heuristics[str(i) + " " + str(j)] = val

    def solve(self):
        fringe = []
        explored = []

        # add start node to fringe
        fringe.append(Node(self.start, 0, self.heuristics[self.start], "none"))
        min_node = Node("", 0, 0, "")

        while self.goal != min_node.coordinate:
            # check if fringe is empty
            if len(fringe) == 0:
                break

            # find minimum f(n)
            min_node = min(fringe, key=lambda fringe: fringe.f_n)

            fringe.remove(min_node)
            # add to min_node to explored
            explored.append(min_node)
            for cell in self.adjacency_list.keys():
                # check we can choose minimum node
                if min_node in self.adjacency_list[cell]:
                    self.adjacency_list[cell].remove(min_node)
            explored_coords = [node.coordinate for node in explored]

            # add adjacency nodes to fringe
            for cell in self.adjacency_list[min_node.coordinate]:
                if cell not in explored_coords:
                    f_n = min_node.path_cost + 1 + self.heuristics[cell]
                    fringe.append(Node(cell, min_node.path_cost + 1, f_n, min_node))

        # min node here is final node
        solution_path = self.find_path(min_node)
        solution_cost = min_node.path_cost
        return solution_path, solution_cost

    def find_path(self, curr_node):
        if curr_node.coordinate == self.goal:
            path = [curr_node.coordinate]

            while curr_node.coordinate != self.start:
                curr_node = curr_node.parent
                path.append(curr_node.coordinate)

            # reverse path
            path.reverse()
            return path
        else:
            return "the route is closed!"
