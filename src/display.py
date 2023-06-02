from world import *
from graph import *
import sys
# Print a world

def print_world(graph, robot, list_balls, passed_balls, previous, frompoint, n=30):
    # Create n*n field
    plt.xlim(0, n)
    plt.ylim(0, n)
    print(len(list_balls))
    list_balls = list_balls + [robot.position]

    if(frompoint >= len(list_balls)-1):
        plt.plot(robot.position[0], robot.position[1], marker="o", label='robot')
        plt.text(robot.position[0] + 0.5, robot.position[1] + 0.5, str(len(list_balls)-1))
        startpos = robot.position
    else:
        startpos = list_balls[frompoint]

    # ¨Print each ball and weight between
    for i in range(len(list_balls)-1):
        
        plt.plot(list_balls[i][0], list_balls[i][1], marker="o", label='ball')
        plt.text(list_balls[i][0] + 0.5, list_balls[i][1] + 0.5, i)

        x_values = [startpos[0], list_balls[i][0]]
        y_values = [startpos[1], list_balls[i][1]]

        appartenance=[(list_balls[i]==x).all() for x in passed_balls]
        value=True
        for bool in appartenance:
            if bool==False:
                value=False
                break
        
        if i==frompoint or value:# or (list_balls[i] in passed_balls).all():

            continue

        plt.plot(x_values, y_values, 'b-')

        mat = graph
        val = mat[previous][frompoint][i]
        plt.text((startpos[0] + list_balls[i][0]) / 2, (startpos[1] + list_balls[i][1]) / 2, str(val))

    # Launch print
    plt.legend()
    plt.show()



def print_path(path, n=30):
    # Create n*n field
    plt.xlim(0, n)
    plt.ylim(0, n)
    x_values = [point[0] for point in path]
    y_values = [point[1] for point in path]
    plt.plot(x_values[1],y_values[1], "r",marker="x",markersize=20)
    plt.plot(x_values[0],y_values[0], "g",marker="*",markersize=20)
    plt.plot(x_values,y_values, "b--")
    plt.plot(x_values, y_values,marker="o", label='ball')
    plt.show()

if __name__ == "__main__":
    print("This file is not runable\n")



