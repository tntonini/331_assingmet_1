import getopt
import sys
from contextlib import redirect_stdout
import heapq
import queue


expanded_count = 0
# Useful defines
LC = 0
LW = 1
LB = 2
RC = 3
RW = 4
RB = 5


def inVisited(visited, element):
    if element in visited:
        return True
    else:
        return False


def makeTree(frontier, key, visited):
    # get initial state
    initial = frontier[0]
    # for dictionary
    # split into left bank and right bank
    left, right = initial
    # get the corresponding variables for the left and right banks
    cLeft, wLeft, bLeft = left.split(',')
    cRight, wRight, bRight = right.split(',')
    # Convert to ints
    cLeft = int(cLeft)
    wLeft = int(wLeft)
    bLeft = int(bLeft)
    cRight = int(cRight)
    wRight = int(wRight)
    bRight = int(bRight)
    # from the current position what happens when...
    visited.append([cLeft, wLeft, bLeft, cRight, wRight, bRight])

    i = 0
    y = 25
    for i in range(25):
        # if on right bank (start bank)
        if bRight == 1:
            # move 1 chicken
            cRight -= 1
            cLeft += 1
            bRight = 0
            bLeft = 1
            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)

                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    print(frontier[key])
                    key += 1
                    # continue
                    cRight += 1
                    cLeft -= 1
                    bRight = 1
                    bLeft = 0
                else:
                    # reset back to before checking if valid
                    cRight += 1
                    cLeft -= 1
                    bRight = 1
                    bLeft = 0
            else:
                # reset back to before checking if valid
                cRight += 1
                cLeft -= 1
                bRight = 1
                bLeft = 0
            # else:
            #     break

            # move 2 chickens
            cRight -= 2
            cLeft += 2
            bRight = 0
            bLeft = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    print(frontier[key])
                    key += 1
                    # continue
                    cRight += 2
                    cLeft -= 2
                    bRight = 1
                    bLeft = 0

                else:
                    # reset back to before checking if valid
                    cRight += 2
                    cLeft -= 2
                    bRight = 1
                    bLeft = 0
            else:
                # reset back to before checking if valid
                cRight += 2
                cLeft -= 2
                bRight = 1
                bLeft = 0

            # move 1 wolf
            wRight -= 1
            wLeft += 1
            bRight = 0
            bLeft = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    print(frontier[key])
                    key += 1
                    # continue
                    wRight += 1
                    wLeft -= 1
                    bRight = 1
                    bLeft = 0

                else:
                    # reset back to before checking if valid
                    wRight += 1
                    wLeft -= 1
                    bRight = 1
                    bLeft = 0
            else:
                # reset back to before checking if valid
                wRight += 1
                wLeft -= 1
                bRight = 1
                bLeft = 0

            # move 2 wolves
            wRight -= 2
            wLeft += 2
            bRight = 0
            bLeft = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    print(frontier[key])
                    key += 1
                    # continue
                    wRight += 2
                    wLeft -= 2
                    bRight = 1
                    bLeft = 0

                else:
                    # reset back to before checking if valid
                    wRight += 2
                    wLeft -= 2
                    bRight = 1
                    bLeft = 0
            else:
                # reset back to before checking if valid
                wRight += 2
                wLeft -= 2
                bRight = 1
                bLeft = 0

            # move 1 wolf 1 chicken
            cRight -= 1
            cLeft += 1
            wRight -= 1
            wLeft += 1
            bRight = 0
            bLeft = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    print(frontier[key])
                    key += 1
                    # continue
                    wRight += 1
                    wLeft -= 1
                    cRight += 1
                    cLeft -= 1
                    bRight = 1
                    bLeft = 0

                else:
                    # reset back to before checking if valid
                    wRight += 1
                    wLeft -= 1
                    cRight += 1
                    cLeft -= 1
                    bRight = 1
                    bLeft = 0
            else:
                # reset back to before checking if valid
                wRight += 1
                wLeft -= 1
                cRight += 1
                cLeft -= 1
                bRight = 1
                bLeft = 0

        # if boat is on left bank
        else:
            # move 1 chicken
            cRight += 1
            cLeft -= 1
            bLeft = 0
            bRight = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    key += 1

                    # continue
                    cRight -= 1
                    cLeft += 1
                    bLeft = 1
                    bRight = 0
                else:
                    # reset back to before checking if valid
                    cRight -= 1
                    cLeft += 1
                    bLeft = 1
                    bRight = 0

            else:
                # reset back to before checking if valid
                cRight -= 1
                cLeft += 1
                bLeft = 1
                bRight = 0

            # move 2 chickens
            cRight += 2
            cLeft -= 2
            bLeft = 0
            bRight = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    key += 1
                    # continue
                    cRight -= 2
                    cLeft += 2
                    bLeft = 1
                    bRight = 0

                else:
                    # reset back to before checking if valid
                    cRight -= 2
                    cLeft += 2
                    bLeft = 1
                    bRight = 0
            else:
                # reset back to before checking if valid
                cRight -= 2
                cLeft += 2
                bLeft = 1
                bRight = 0

            # move 1 wolf
            wRight += 1
            wLeft -= 1
            bLeft = 0
            bRight = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    key += 1
                    # continue
                    wRight -= 1
                    wLeft += 1
                    bLeft = 1
                    bRight = 0

                else:
                    # reset back to before checking if valid
                    wRight -= 1
                    wLeft += 1
                    bLeft = 1
                    bRight = 0
            else:
                # reset back to before checking if valid
                wRight -= 1
                wLeft += 1
                bLeft = 1
                bRight = 0

            # move 2 wolves
            wRight += 2
            wLeft -= 2
            bLeft = 0
            bRight = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    key += 1
                    # continue
                    wRight -= 2
                    wLeft += 2
                    bLeft = 1
                    bRight = 0

                else:
                    # reset back to before checking if valid
                    wRight -= 2
                    wLeft += 2
                    bLeft = 1
                    bRight = 0
            else:
                # reset back to before checking if valid
                wRight -= 2
                wLeft += 2
                bLeft = 1
                bRight = 0

            # move 1 wolf 1 chicken
            cRight += 1
            cLeft -= 1
            wRight += 1
            wLeft -= 1
            bLeft = 0
            bRight = 1

            if(inVisited(visited, [cLeft, wLeft, bLeft, cRight, wRight, bRight]) == False):
                visited.append(
                    [cLeft, wLeft, bLeft, cRight, wRight, bRight])

                valid = isValidMove(cLeft, wLeft, bLeft,
                                    cRight, wRight, bRight)
                if valid:
                    frontier[key] = [cLeft, wLeft,
                                     bLeft, cRight, wRight, bRight]
                    key += 1
                    # continue
                    cRight -= 1
                    cLeft += 1
                    wRight -= 1
                    wLeft += 1
                    bLeft = 1
                    bRight = 0

                else:
                    # reset back to before checking if valid
                    cRight -= 1
                    cLeft += 1
                    wRight -= 1
                    wLeft += 1
                    bLeft = 1
                    bRight = 0
            else:
                # reset back to before checking if valid
                cRight -= 1
                cLeft += 1
                wRight -= 1
                wLeft += 1
                bLeft = 1
                bRight = 0
        i += 1
    return frontier


def isValidMove(cLeft, wLeft, bLeft, cRight, wRight, bRight):
    if cLeft >= 0 and wLeft >= 0 and cRight >= 0 and wRight >= 0 and (cLeft >= wLeft or cLeft == 0) and (cRight >= wRight or cRight == 0):
        return True
    else:
        return False


def bfs(initialState, goalState, output):
    # Convert list of strings with commas into a usable list of ints
    initial = []
    for element in initialState:
        element = element.replace(',', '')
        for item in element:
            initial.append(int(item))

    goal = []
    for element in goalState:
        element = element.replace(',', '')
        for item in element:
            goal.append(int(item))

    print(initial)
    print(goal)
    # output is a filename

    frontier = queue.Queue()
    frontier.put(initial)

    explored = []
    numNodes = 0

    while frontier is not None:
        currentNode = frontier.get()
        if currentNode in explored:
            continue
        if currentNode == goal:
            print("Goal reached!!!")
            print(currentNode)
            return
        print(currentNode)
        children = expand(currentNode, frontier, explored)

        for child in children:
            numNodes += 1
            frontier.put(child)
        explored.append(currentNode)
        print("Added", currentNode, "to explored")




# *****************************************************************************


def isValidState(state):
    # No negative animals
    if (state[LC] < 0) or (state[LW] < 0) or (state[RC] < 0) or (state[RW] < 0):
        return False
    # Handle left bank eats
    if (state[LC] < state[LW]) and (state[LC] != 0):
        return False
    if (state[RC] < state[RW]) and (state[RC] != 0):
        return False
    return True


def printExplored(explored):
    index = 0
    for list in explored:
        print(index, list)
        index += 1



def dfs(initialState, goalState, output):
    with open(output, "w") as f:
        # output is a filename
        initial = []
        for line in initialState:
            for var in line.split(","):   # store every item as its own element,
                # even if there are multiple on 1 line
                initial.append(int(var))
        print("Start: ", initial)
        goal = []
        for line in goalState:
            for var in line.split(","):   # store every item as its own element,
                goal.append(int(var))  # even if there are multiple on 1 line
        print("Goal: ", goal)

        frontier = []
        frontier.insert(0, initial)
        explored = []
        explored_count = 0  # A count of how many nodes have been explored/popped
        while frontier:
            currentNode = frontier.pop(0)
            if currentNode in explored:  # duplicates are allowed in the frontier
                continue
            explored.append(currentNode)
            # print(explored_count,"Popped",currentNode,"off frontier") #DEBUG
            if currentNode == goal:
                print("Nodes explored:", explored_count)
                print("Path length:",explored_count)
                print("# [LC LW LB RC RW RB]")
                printExplored(explored)

                f.write("Nodes explored: "+str(explored_count)+"\n")
                f.write("Path length: "+str(explored_count)+"\n")
                f.write("[LC LW LB RC RW RB]\n")
                for state in explored:
                    f.write(str(state)+"\n")
                return
            # explored.append(currentNode)
            explored_count += 1
            children = expand(currentNode, frontier, explored)

            for child in children:
                frontier.insert(0, child)

        print("no solution found")
        print("Nodes explored:", explored_count)
        f.write("no solution found\n")
        f.write("Nodes explored:"+str(explored_count)+"\n")
        return


def expand(state, frontier, explored):
    # expands a state, returning up to 5 unexplored leaves
    leaves = []
    # Process:
    # generate leaf
    # if valid and unexplored, add to leaves[] and return leaves[]

    # 1: 1 chicken in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LC] -= 1
        generated[RC] += 1
    else:
        generated[LC] += 1
        generated[RC] -= 1

    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank

    if isValidState(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 2: 2 chickens in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LC] -= 2
        generated[RC] += 2
    else:
        generated[LC] += 2
        generated[RC] -= 2
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidState(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 1 wolf in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LW] -= 1
        generated[RW] += 1
    else:
        generated[LW] += 1
        generated[RW] -= 1
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidState(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 1 wolf 1 chicken
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LW] -= 1
        generated[LC] -= 1
        generated[RW] += 1
        generated[RC] += 1
    else:  # if boat is on right side
        generated[LW] += 1
        generated[LC] += 1
        generated[RW] -= 1
        generated[RC] -= 1
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidState(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 5: 2 wolves in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LW] -= 2
        generated[RW] += 2
    else:
        generated[LW] += 2
        generated[RW] -= 2
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidState(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)
    # print("Expand() found ", len(leaves), "leaves"

    return leaves


def iddfs(initialState, goalState, output):
    numNodes = 0
    # Convert list of strings with commas into a usable list of ints
    initial = []
    for element in initialState:
        element = element.replace(',', '')
        for item in element:
            initial.append(int(item))

    goal = []
    for element in goalState:
        element = element.replace(',', '')
        for item in element:
            goal.append(int(item))
    print(initial)
    print(goal)
    print(initial[3])
    frontier = []
    current = 0
    frontier.insert(0, initial)
    explored = []

    while frontier:
        currentNode = frontier.pop()

        children = expand(currentNode, frontier, explored)

        for child in children:
            frontier.insert(0, child)
        explored.append(currentNode)
        # print("Added", currentNode, "to explored")

    for depth in range(100):
        goalNode = recursive_iddfs(explored, current, goal, depth, numNodes, output)
        if goalNode == True:
            print("goalNode")


def printIDDFS(explored, depth, numNodes, output):
    with open(output, "w") as f:
        print("Nodes explored:", numNodes)
        print("Depth: ", depth)
        printExplored(explored)

        f.write("Nodes explored: "+str(numNodes)+"\n")
        f.write("Path length: "+str(numNodes)+"\n")
        f.write("Depth: "+str(depth)+"\n")
        f.write("[LC LW LB RC RW RB]\n")
        for state in explored:
            f.write(str(state)+"\n")
    exit()


def recursive_iddfs(explored, current, goal, depth, numNodes, output):
    if explored[current] == goal:
        printIDDFS(explored, depth, numNodes, output)
        return True  # found the goal node
    if depth <= 0:
        return False

    numNodes += 1
    if(recursive_iddfs(explored, current + 1, goal, depth - 1, numNodes, output)):
        return True
    return False



def heuristic(n,goal): # calculates h(n) for input state n as a list
    if n == goal: return 0
    # assume animals start on right bank and move to left bank
    return max(1,(n[RC] + n[RW])-1)
    # subtract 1, becuase up to 2 animals can be moved at once for final move
    # 1 animal left: returns 1
    # 2 animals left: returns 1
    # 3 animals left: returns 2 (an underestimate)

def listToString(list): # helper function to let nodes be dict keys as strings
    string_list = [str(int) for int in list]
    return ",".join(string_list)

def astar(initialState, goalState, output):
    with open(output, "w") as f:
        # output is a filename
        initial = []
        for line in initialState:
            for var in line.split(","):   # store every item as its own element,
                # even if there are multiple on 1 line
                initial.append(int(var))
        print("Start: ", initial)
        goal = []
        for line in goalState:
            for var in line.split(","):   # store every item as its own element,
                goal.append(int(var))  # even if there are multiple on 1 line
        print("Goal: ", goal)

        frontier = {} # Frontier is a dictionary with key = f(n) and value = state
        parent = {} # Parent is a dictionary with key = node and value = parent node
        g_set = {} # Key = node, value = cost to get to n from start
        f_set = {} # f(n) = g(n) + h(n)
        current = listToString(initial)
        frontier[current] = 0 # add initial element to the frontier
        parent[current] = None
        f_set[current] = heuristic(initial,goal)
        explored = [] # list of states explored, with lists representing states
        explored_count = 0  # A count of how many nodes have been explored/popped

        while frontier: #while frontier isn't empty
            #min(frontier) is the lowest f(n), so frontier[min(frontier)] is the best node
            key = min(frontier.values())
            del frontier[key]
            print("Popped",key,"with heuristic",key)

            #currentNode = frontier.pop(0)
            if currentNode in explored:  # duplicates are allowed in the frontier
                continue
            explored.append(currentNode)
            # print(explored_count,"Popped",currentNode,"off frontier") #DEBUG
            if currentNode == goal:
                print("Nodes explored:", explored_count)
                printExplored(explored)

                f.write("Nodes explored: "+str(explored_count)+"\n")
                f.write("Path length: "+str(explored_count)+"\n")
                f.write("[LC LW LB RC RW RB]\n")
                for state in explored:
                    f.write(str(state)+"\n")
                return
            # explored.append(currentNode)
            explored_count += 1
            children = expand(currentNode, frontier, explored)

            for child in children:
                new_g = g[parent] + 1
                # if new_g < g[child]
                frontier[heuristic(child,goal)] = child

        print("no solution found")
        print("Nodes explored:", explored_count)
        f.write("no solution found\n")
        f.write("Nodes explored:"+str(explored_count)+"\n")
        return


def main():

    n = len(sys.argv)

    if(n < 4):
        print("Must be in form < initial state file > < goal state file > < mode > < output file >")
        exit()

    initialStateFile = sys.argv[1]
    goalStateFile = sys.argv[2]
    mode = sys.argv[3]
    output = sys.argv[4]

    initialState = open(initialStateFile, "r")
    initialState = initialState.readlines()
    # remove newlines
    initialState = list(
        map(str.strip, initialState))
    # print("initialState:",initialState)

    goalState = open(goalStateFile, "r")
    goalState = goalState.readlines()
    # remove newlines
    goalState = list(
        map(str.strip, goalState))
    # print(goalState)

    if mode == "bfs":
        bfs(initialState, goalState, output)
    elif mode == "dfs":
        dfs(initialState, goalState, output)
    elif mode == "iddfs":
        iddfs(initialState, goalState, output)
    elif mode == "astar":
        astar(initialState, goalState, output)
    else:
        print("Must be in form < initial state file > < goal state file > < mode > < output file >")


if __name__ == "__main__":
    main()
