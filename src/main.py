from graph import *
from world import *
from display import *
import sys

if __name__ == "__main__":

    if len(sys.argv) < 6:
        print("Missing arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed, 5- algo ('opt' or 'close'))")
        exit(1)

    if len(sys.argv) > 6:
        print("To much arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed, 5- algo ('opt' or 'close'))")
        exit(1)

    if sys.argv[5] == "opt":
        algo = path_opt
    elif sys.argv[5] == "close":
        algo = shortest_path
    else:
        print("Mauvais argument pour décider de l'algorithme : 'opt' le chemin optimal, 'close' pour le solution approchée")
        exit()

    N = int(sys.argv[2])

    robot, list_balls = init_world(sys.argv[1], int(
        sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    graph = init_graph(list_balls, robot)

    passed_balls = [np.array([robot.position[0], robot.position[1]-0.5])]

    print_world(graph, robot, list_balls, passed_balls,
                previous=0, frompoint=len(list_balls), n=N)

    path = algo(graph, list_balls, robot)
    print_path(path, N)
    
