import getopt
import sys
from contextlib import redirect_stdout


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

    # Psuedocode from lecture for graph search
    # function GRAPH-SEARCH(problem) returns a solution, or failure
    #     initialize the frontier using the initial state of problem
    #     initialize the explored set to be empty
    #     loop do
    #         if the fronteir is empy then return failure
    #         choose a elage node and remove it from the frontier
    #         if the node contains a goal state then return the corresponding solution
    #         add the node to the explored set
    #         expand the chosen node, adding the resulting nodes to the frontier
    #             only if not in the frontier or explored set

    # initialize dictionary
    element = 0
    frontier = {}
    explored = []
    frontier[element] = initialState

    # while initialState != goalState:
    if bool(frontier) == False:
        sys.exit("Frontier is empty")
    frontier = makeTree(frontier, element, explored)

    print(frontier)




class node:
    def __init__(self, state, children = None):
        self.state = state
        self.children = children or []
        self.parent = None
        for child in self.children:
            child.parent = self


class gameState: #UNUSED, NOT WORTH
    def __init__(state):
        self.state = state
        # self.cLeft = cLeft
        # self.wLeft = wLeft
        # self.bLeft = bLeft
        # self.cRight = cRight
        # self.wRight = wRight
        # self.bRight = bRight

    def __eq__(self,other):
        return self.state == other.state

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

def printExplored(explored):
    index = 0
    for list in explored:
        print(index,list)
        index += 1

# handler for recursive dfs
def dfs(initialState, goalState,output):
    with open(output,"w") as f:
        # output is a filename
        initial = []
        for line in initialState:
            for var in line.split(","):   # store every item as its own element,
                  initial.append(int(var)) # even if there are multiple on 1 line
        print("Start: ",initial)
        goal = []
        for line in goalState:
            for var in line.split(","):   # store every item as its own element,
                  goal.append(int(var)) # even if there are multiple on 1 line
        print("Goal: ",goal)




        frontier = []
        frontier.insert(0,initial)
        explored = []
        explored_count = 0 # A count of how many nodes have been explored/popped
        while frontier:
            currentNode = frontier.pop(0)
            if currentNode in explored: # duplicates are allowed in the frontier
                continue
            explored.append(currentNode)
            # print(explored_count,"Popped",currentNode,"off frontier") #DEBUG
            if currentNode == goal:
                print("Nodes explored:",explored_count)
                printExplored(explored)

                f.write("Nodes explored: "+str(explored_count)+"\n")
                f.write("Path length: "+str(explored_count)+"\n")
                f.write("[LC LW LB RC RW RB]\n")
                for state in explored:
                    f.write(str(state)+"\n")
                return
            # explored.append(currentNode)
            explored_count += 1
            children = expand(currentNode,frontier, explored)

            for child in children:
                frontier.insert(0,child)

        print("no solution found")
        print("Nodes explored:",explored_count)
        f.write("no solution found\n")
        f.write("Nodes explored:"+str(explored_count)+"\n")
        return





def expand(state,frontier,explored):
    # expands a state, adding up to 5 unexplored leaves to the Frontier
    leaves = []
    LC = 0
    LW = 1
    LB = 2
    RC = 3
    RW = 4
    RB = 5
    # Process:
    # generate leaf
    # if valid and unexplored, add to frontier


    # 1: 1 chicken in the boat
    generated = state.copy()
    if(generated[LB]): # if boat is on left side
        generated[LC] -= 1
        generated[RC] += 1
    else:
        generated[LC] += 1
        generated[RC] -= 1
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 2: 2 chickens in the boat
    generated = state.copy()
    if(generated[LB]): # if boat is on left side
        generated[LC] -= 2
        generated[RC] += 2
    else:
        generated[LC] += 2
        generated[RC] -= 2
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 1 wolf in the boat
    generated = state.copy()
    if(generated[LB]): # if boat is on left side
        generated[LW] -= 1
        generated[RW] += 1
    else:
        generated[LW] += 1
        generated[RW] -= 1
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 1 wolf 1 chicken
    generated = state.copy()
    if(generated[LB]): # if boat is on left side
        generated[LW] -= 1
        generated[LC] -= 1
        generated[RW] += 1
        generated[RC] += 1
    else: # if boat is on right side
        generated[LW] += 1
        generated[LC] += 1
        generated[RW] -= 1
        generated[RC] -= 1
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)

    # 5: 2 wolves in the boat
    generated = state.copy()
    if(generated[LB]): # if boat is on left side
        generated[LW] -= 2
        generated[RW] += 2
    else:
        generated[LW] += 2
        generated[RW] -= 2
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        # print("Added leaf:",generated)
        leaves.append(generated)
    # print("Expand() found ", len(leaves), "leaves")

    return leaves



def iddfs(initialState, goalState, output):
    print("iddfs")


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
