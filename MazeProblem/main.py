from MazeSolver import Maze


def main():
    maze_cols = 4
    maze_rows = 4
    path = [[0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]]
    start = "0 0"
    goal = "3 3"
    maze = Maze(maze_rows, maze_cols, path, start, goal)
    path, cost = maze.solve()

    print("Cost is: {}".format(cost))
    print("Path is: {}".format(path))


if __name__ == "__main__":
    main()
