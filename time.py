from graph import *
from world import *
from time import *
import matplotlib.pyplot as plt


def gen_times_for_opt():
    times = []
    
    robot, list_balls = init_world("./timeterrain/timeterrain2.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain3.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain4.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain5.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain6.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain7.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain8.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain9.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain10.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain11.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain12.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    path_opt(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    return times



def gen_times_for_shortest():
    times = []

    robot, list_balls = init_world("./timeterrain/timeterrain2.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain3.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain4.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain5.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain6.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain7.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain8.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain9.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain10.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain11.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    robot, list_balls = init_world("./timeterrain/timeterrain12.csv", 50, 2, 2)
    graph = init_graph(list_balls + [robot.position], robot)
    start_time = perf_counter()
    shortest_path(graph, list_balls, robot)
    end_time = perf_counter()
    times.append(end_time - start_time)

    return times

if __name__ == "__main__":
    plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], gen_times_for_opt(),"b+",label="optimal_path")
    plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], gen_times_for_shortest(),"r-",label="close_to_close_path")
    plt.xlabel("Nombre de balles")
    plt.ylabel("Temps de calcul (en s)")
    plt.yscale("log")
    plt.legend()
    plt.title("Temps de calcul du plus court chemin en fonction du nombre de balles à ramasser")
    plt.show()