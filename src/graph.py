import numpy as np
import itertools

# Initializes the graph
def init_graph(list_nodes, robot):
    list_nodes = list_nodes + [robot.position]
    size = len(list_nodes)

    # First fill with zeros
    graph = np.zeros((size, size, size))

    # Foreach couple (i,j) where i different j initialize length to -1
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if i != j:
                    graph[layer][i][j] = -1

    # If from pos equals to end pos set length to 0
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if i == layer or j == layer:
                    graph[layer][i][j] = 0
                    
    # Filling the graph with angles
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if layer != i and i != j and layer != j:
                    if graph[layer][i][j] == -1:
                        graph[layer][i][j] = weight(
                            layer, i, j, list_nodes, robot)

    return graph


# Calculate the time it takes to go from current to future node coming from previous node.
def weight(previous_node, current_node, future_node, list_nodes, robot):
    # Calculate angle between 3 points a, b, c
    if isinstance(previous_node, int):
        a = list_nodes[previous_node]
    else:
        a = previous_node
    b = list_nodes[current_node]
    c = list_nodes[future_node]

    ba = b - a
    bc = c - b

    # if abs(np.linalg.norm(ba) * np.linalg.norm(bc)) < 1e-5:
    #     return 0

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    if cosine_angle > 1:
        cosine_angle = 1
    elif cosine_angle < -1:
        cosine_angle = -1
    angle = np.arccos(cosine_angle)

    # Distance between current and future point
    distance = np.linalg.norm(bc)
    return angle / robot.rot_speed + distance / robot.mv_speed

# Finds the optimal path by going through the tree of paths
def path_opt(graph, list_balls, robot):
    init_pos = robot.position
    perm = itertools.permutations(range(len(list_balls)))
    weight_min = float('inf')
    exceed_weight = False
    path_min = []
    list_balls.append(init_pos)
    list_balls.append(np.array([init_pos[0], init_pos[1] - 0.5]))

    # for all possible paths (p is list idx of balls in list_balls)
    for p in perm:
        p = list(p)
        # len(list_balls) - 2 is for init_pos (robot initial position)
        p.insert(0, len(list_balls) - 2)
        # adding because we start from here and we have to finish here
        p.insert(0, len(list_balls) - 2)
        p.append(len(list_balls) - 2)

        path = [init_pos]

        sum_weight = 0

        # get total weight
        # if weight > weight_min : STOP
        for i in range(len(list_balls) - 1):
            # print(sum_weight)
            if i == 0:
                sum_weight = weight(len(list_balls) - 1, len(list_balls) - 2, p[i + 2], list_balls, robot)
            # weight of the edge for coming from p[i], is in p[i + 1] and going to p[i + 2]
            else:
                sum_weight += graph[p[i]][p[i + 1]][p[i + 2]]
            # + 2 because the first 2 idx are for init_pos
            path.append(list_balls[p[i + 2]])

            if sum_weight > weight_min:
                exceed_weight = True
                break

        if not exceed_weight:
            weight_min = sum_weight
            path_min = path

        exceed_weight = False

    return path_min


# Finds the shortest path going from a node to the closest next node
def shortest_path(graph, list_balls, robot):
    path_min = []  # Initialize the list to store the minimum path
    init_pos = robot.position
    list_nodes = list_balls + [init_pos] + \
        [np.array([init_pos[0], init_pos[1] - 0.5])]
    passed_balls = [np.array([init_pos[0], init_pos[1] - 0.5])]
    already_chosen_balls = []
    # Initialize variables to track previous, current, and next nodes
    (previous, current, next) = (-1, -1, -1)

    sum = 0  # Initialize the sum of weights

    min = float('inf')  # Initialize the minimum weight as infinity
    for i in range(len(list_balls)):
        # Find the ball with the minimum weight from the initial position
        if weight(len(list_nodes) - 1, len(list_nodes) - 2, i, list_nodes, robot) < min:
            min = weight(len(list_nodes) - 1, len(list_nodes) -
                         2, i, list_nodes, robot)
            (previous, current, next) = (
                len(list_nodes) - 1, len(list_nodes) - 2, i)
    sum += min

    passed_balls.append(init_pos)
    already_chosen_balls.append(current)
    already_chosen_balls.append(next)

    goto_node = 0
    while len(already_chosen_balls) - 1 < len(list_balls):
        # Iterate until all balls are chosen
        layer = graph[current]
        weights = layer[next]
        min = float('inf')
        for i in range(len(weights) - 1):
            if i not in already_chosen_balls:
                # Find the ball with the minimum weight from the current ball
                if weights[i] < min:
                    min = weights[i]
                    goto_node = i
        sum += min

        (previous, current, next) = (current, next, goto_node)
        already_chosen_balls.append(next)

    sum += weight(current, next, already_chosen_balls[0], list_nodes, robot)
    already_chosen_balls.append(already_chosen_balls[0])
    path_min = [list_nodes[i]
                for i in already_chosen_balls]  # Construct the minimum path

    return path_min


if __name__ == "__main__":
    from world import *

    robot, list_balls = init_world("terrain.csv")
    graph = init_graph(list_balls, robot)
    path = shortest_path(graph, list_balls, robot)
    print(path)
    print("This file is not runable\n")
