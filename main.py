import getopt
import sys
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


class gameState:  # UNUSED, NOT WORTH
    def __init__(cLeft, wLeft, bLeft, cRight, wRight, bRight):
        self.cLeft = cLeft
        self.wLeft = wLeft
        self.bLeft = bLeft
        self.cRight = cRight
        self.wRight = wRight
        self.bRight = bRight

    def __eq__(self, other):
        pass

    def isValidState(self):
        if cLeft >= 0 and wLeft >= 0 and cRight >= 0 and wRight >= 0 and (cLeft >= wLeft or cLeft == 0) and (cRight >= wRight or cRight == 0):
            return True
        else:
            return False

    def print(self):
        return

# *****************************************************************************


def isValidMove(state):
    # No negative animals
    if (state[LC] < 0) or (state[LW] < 0) or (state[RC] < 0) or (state[RW] < 0):
        return False
    # Handle left bank eats
    if (state[LC] < state[LW]) and (state[LC] != 0):
        return False
    if (state[RC] < state[RW]) and (state[RC] != 0):
        return False
    return True


# handler for recursive dfs
def dfs(initialState, goalState, output):
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
    frontier = []
    frontier.insert(0, initial)
    explored = []
    while frontier is not None:
        currentNode = frontier.pop()
        if currentNode in explored:
            continue
        if currentNode == goal:
            return
        print(currentNode)
        children = expand(currentNode, frontier, explored)

        for child in children:
            frontier.insert(0, child)
        explored.append(currentNode)
        print("Added", currentNode, "to explored")
    # # counter = 0 # Number of nodes expanded.
    #
    # #implement the graph-search version, which is complete
    # frontier = []
    # frontier.insert(0,initial) # add initial state / root
    # explored = []
    # global expanded_count
    # expanded_count = 0
    # dfs_recursive(frontier,goalState,explored)


def dfs_recursive(frontier, goalState, explored):
    # frontier: a list of states in a LIFO queue
    # goalState: a list containing the goal state
    # explored: a list of states that have been explored (popped)
    # output: a list of states tracing back to the root???
    global expanded_count

    # # Check if frontier empty
    while frontier is not empty:
        # pop off frontier top of
        # TA said compare node with goal when its popped
        currentNode = frontier.pop()  # pop off front of LIFO for DFS
        # global expanded_count += 1 # Increment count between pop and expansion
        # Check if goal is reached
        if currentNode == goalState:
            print("Goal reached!!!")
            sys.exit("Goal reached!!!")
            return
        # Add current node to explored
        explored.append(currentNode)
        print("Added", currentNode, "to explored")
        # Increment # nodes counter
        expanded_count += 1

        # Call expand function
        # print("Frontier before expand:",frontier)
        discovered = expand(currentNode, frontier, explored)
        # print("Frontier after expand:",frontier)

        # call DFS recursively
        for leaf in discovered:
            dfs_recursive(frontier, goalState, explored)


def expand(state, frontier, explored):
    # expands a state, adding up to 5 unexplored leaves to the Frontier
    leaves = []
    global LC
    LW = 1
    LB = 2
    RC = 3
    RW = 4
    RB = 5
    # Process:
    # generate leaf
    # if valid and unexplored, add to frontier

    # 1 chicken in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LC] -= 1
        generated[RC] += 1
    else:
        generated[LC] += 1
        generated[RC] -= 1
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    # print(generated not in explored)
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.insert(0, generated)

    # 2 chickens in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LC] -= 2
        generated[RC] += 2
    else:
        generated[LC] += 2
        generated[RC] -= 2
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.insert(0, generated)

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
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.insert(0, generated)

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
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.insert(0, generated)

    # 2 wolves in the boat
    generated = state.copy()
    if(generated[LB]):  # if boat is on left side
        generated[LW] -= 2
        generated[RW] += 2
    else:
        generated[LW] += 2
        generated[RW] -= 2
    generated[LB] ^= 1  # swap boat bank
    generated[RB] ^= 1  # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.insert(0, generated)
    # print("Expand() found ", len(leaves), "leaves")
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
        goalNode = recursive_iddfs(explored, current, goal, depth, numNodes)
        if goalNode == True:
             print("goalNode")

def recursive_iddfs(explored, current, goal, depth, numNodes):
    if explored[current] == goal:
        print("Goal reached!!!")
        print(explored[current])
        return True #found the goal node
    if depth <= 0:
        return False

    numNodes += 1
    if(recursive_iddfs(explored, current + 1, goal, depth - 1, numNodes)):
        return True
    return False

            

def astar(initialState, goalState, output):
    print("astar")


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
    print("initialState:", initialState)

    goalState = open(goalStateFile, "r")
    goalState = goalState.readlines()
    # remove newlines
    goalState = list(
        map(str.strip, goalState))
    print(goalState)

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
