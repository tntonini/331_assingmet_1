import getopt
import sys


def bfs(initialState, goalState, output):
    print("bfs")


def dfs(initialState, goalState, output):
    print("dfs")


def iddfs(initialState, goalState, output):
    print("iddfs")


def astar(initialState, goalState, output):
    print("astar")


def main():
    initialState = sys.argv[1]
    goalState = sys.argv[2]
    mode = sys.argv[3]
    output = sys.argv[4]

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
