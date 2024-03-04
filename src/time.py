from graph import *
from world import *
from time import *
import matplotlib.pyplot as plt


def gen_times_for_opt():
    times = []
    
    robot, list_balls = init_world("./timeterrain/timeterrain2.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain3.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain4.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain5.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain6.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain7.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain8.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain9.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain10.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain11.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    return times



def gen_times_for_shortest():
    times = []

    robot, list_balls = init_world("./timeterrain/timeterrain2.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain3.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain4.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain5.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain6.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain7.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain8.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain9.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain10.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain11.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)
    return times

def gen_big_times_for_shortest():
    times = []

    robot, list_balls = init_world("./timeterrain/timeterrain5.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain10.csv", 50, 2, 2)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    list_balls = np.random.randint(0, 1000, size = (50, 2), dtype=np.int64)
    robot = Robot(np.array([500, 500]), 0, 100, 2)
    for i in range(len(list_balls)):
        if np.all(list_balls[i] == robot.position):
            list_balls.remove(b)
            print(b)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    list_balls = np.random.randint(0, 10000, size = (200, 2), dtype=np.int64)
    robot = Robot(np.array([5000, 5000]), 0, 1000, 2)
    list_balls = np.unique(list_balls, axis=0)
    for i in range(len(list_balls)):
        if np.all(list_balls[i] == robot.position):
            list_balls.remove(b)
            print(b)
    start_time = perf_counter()
    graph = init_graph(list_balls + [robot.position], robot)
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    return times

if __name__ == "__main__":
    # plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], gen_times_for_opt(),"b+",label="optimal_path")
    # plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], gen_times_for_shortest(),"r-",label="close_to_close_path")
    # plt.xlabel("Nombre de balles")
    # plt.ylabel("Temps de calcul (en s)")
    # plt.yscale("log")
    # plt.legend()
    # plt.title("Temps de calcul du plus court chemin en fonction du nombre de balles à ramasser")
    # plt.show()
    plt.plot([5, 10, 50, 200], gen_big_times_for_shortest(),"r-",label="close_to_close_path")
    plt.xlabel("Nombre de balles")
    plt.ylabel("Temps de calcul (en s)")
    plt.yscale("log")
    plt.legend()
    plt.title("Temps de calcul du plus court chemin en fonction du nombre de balles à ramasser")
    plt.show()