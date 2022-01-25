x_capacity = int(input("Enter the capacity of x jug: "))
y_capacity = int(input("Enter the capacity of y jug: "))

x_initial = 0  # initial
y_initial = 0  # initial

x_goal = int(input("Enter the goal amount in x jug: "))
y_goal = int(input("Enter the goal amount in y jug: "))

state_space = {}
open_list = [(0, 0)]  # nodes not expanded
closed_list = []  # nodes expanded
# When we dequeue from open_list elements go in close_list

while (x_goal, y_goal) not in closed_list or len(open_list) != 0:

    (x_initial, y_initial) = open_list.pop(0)

    if (x_initial, y_initial) not in closed_list:
        l = []
        state_space[(x_initial, y_initial)] = l

        if x_initial < x_capacity:
            l.append((x_capacity, y_initial))
            open_list.append((x_capacity, y_initial))

        if y_initial < y_capacity:
            l.append((x_initial, y_capacity))
            open_list.append((x_initial, y_capacity))

        if x_initial > 0:
            l.append((0, y_initial))
            open_list.append((0, y_initial))

        if y_initial > 0:
            l.append((x_initial, 0))
            open_list.append((x_initial, 0))

        if x_initial > 0 and y_initial < y_capacity:
            if x_initial + y_initial > y_capacity:
                l.append((x_initial + y_initial - y_capacity, y_capacity))
                open_list.append((x_initial + y_initial - y_capacity, y_capacity))
            else:
                l.append((0, x_initial + y_initial))
                open_list.append((0, x_initial + y_initial))

        if x_initial < x_capacity and y_initial > 0:
            if x_initial + y_initial > x_capacity:
                l.append((x_capacity, x_initial + y_initial - x_capacity))
                open_list.append((x_capacity, x_initial + y_initial - x_capacity))
            else:
                l.append((x_initial + y_initial, 0))
                open_list.append((x_initial + y_initial, 0))

        closed_list.append((x_initial, y_initial))
        if ((x_goal, y_goal) == (x_initial, y_initial)): break

for key, value in state_space.items():
    print("Selected vertex is ", key, "with children ", value)

print("Path of traversal is: ", closed_list)