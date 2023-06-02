from graph import *
from world import *
from display import *
import sys

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("Missing arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    if len(sys.argv) > 5:
        print("To much arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    robot, list_balls = init_world(sys.argv[1], int(
        sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    graph = init_graph(list_balls, robot)

    print(len(list_balls), len(graph))

    passed_balls = [np.array([robot.position[0], robot.position[1]-0.5])]

    #print_world(graph, robot, list_balls, passed_balls,previous=0, frompoint=len(list_balls))

    path = shortest_path(graph, list_balls, robot)
    print_path(path)
    
