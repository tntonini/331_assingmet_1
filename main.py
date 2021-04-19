import getopt
import sys


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


class gameState: #UNUSED, NOT WORTH
    def __init__(cLeft, wLeft, bLeft, cRight, wRight, bRight):
        self.cLeft = cLeft
        self.wLeft = wLeft
        self.bLeft = bLeft
        self.cRight = cRight
        self.wRight = wRight
        self.bRight = bRight

    def __eq__(self,other):
        pass

    def isValidState(self):
        if cLeft >= 0 and wLeft >= 0 and cRight >= 0 and wRight >= 0 and (cLeft >= wLeft or cLeft == 0) and (cRight >= wRight or cRight == 0):
            return True
        else:
            return False


    def print(self):
        return


# handler for recursive dfs
def dfs(initialState, goalState,output):
    # Convert list of strings with commas into a usable list of ints
    initial = []
    for element in initialState:
        element = element.replace(',','')
        for item in element:
            initial.append(int(item))

    goal = []
    for element in goalState:
        element = element.replace(',','')
        for item in element:
            goal.append(int(item))
    print(initial)
    print(goal)



    # output is a filename

    counter = 0 # Number of nodes expanded.

    #implement the graph-search version, which is complete
    frontier = []
    frontier.insert(0,initial) # add initial state / root
    explored = []


    print("Starting recursive calls...")
    dfs_recursive(frontier,goalState,explored)




def dfs_recursive(frontier,goalState,explored):
    # frontier: a list of states in a LIFO queue
    # goalState: a list containing the goal state
    # explored: a list of states that have been explored (popped)
    # output: a list of states tracing back to the root???


    # if frontier empty, return fail
    if frontier is None:
        print("Frontier empty! Failed.")

    #pop frontier.
    # TA said compare node with goal when its popped
    currentNode = frontier.pop() # pop off front of LIFO for DFS
    expanded_count += 1 # Increment count between pop and expansion
    # Check if goal is reached
    if currentNode == goalState:
        print("Goal reached")
        return
    explored.append(currentNode)

    expand(currentNode,frontier,explored)



def expand(state,frontier,explored): # expands a state, generating up to 5 unexplored leaves to add to the Frontier
    print("Expanding",state)
    print("Frontier:",frontier)
    LC = 0
    LW = 1
    LB = 2
    RC = 3
    RW = 4
    RB = 5
    # Process:
    # generate leaf
    # check if valid
    # if explored, don't add to frontier


    # 1 chicken in the boat
    generated = state
    if(generated[LB]): # if boat is on left side
        generated[LC] -= 1
        generated[RC] += 1
    else:
        generated[LC] += 1
        generated[RC] -= 1
    generated[LB] ^= 1 # swap boat bank
    generated[RB] ^= 1 # swap boat bank
    if isValidMove(generated) and generated not in explored:
        frontier.insert(0,node)

    # 2 chickens in the boat
    frontier.insert(0,node)
    frontier.insert(0,node) # 1 wolf in the boat
    frontier.insert(0,node) # 1 wolf 1 chicken
    frontier.insert(0,node) # 2 wolves in the boat

    print("New Frontier:", frontier)
    pass





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
    print(initialState)

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
