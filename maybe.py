# Import networkx library for graph operations
import networkx as nx


def read_input(filename):
    test_cases = []
    with open(filename) as f:
        while True:
            # Read the first line of each test case and split it into N and M
            line = f.readline().strip()
            if line == "0 0":
                break  # End of input
            N, M = map(int, line.split())
            # Read the next M lines and store them as a list of tuples (A, B, F)
            decisions = []
            for _ in range(M):
                A, B, F = map(int, f.readline().split())
                decisions.append((A, B, F))
            # Append the test case as a tuple (N, M, decisions) to the list of test cases
            test_cases.append((N, M, decisions))
    return test_cases


# Define a function that returns the sum of weights of a path
def get_weight(G, path):
    weight = 0
    for i in range(len(path) - 1):
        a = G.get_edge_data(path[i], path[i + 1])
        if a is None:
            continue
        weight += G.get_edge_data(path[i], path[i + 1])["weight"]
    return weight


def get_weight_cycle(G, path):
    weight = 0
    path = [element for i, tup in enumerate(path) for element in (tup if i == len(path) - 1 else [tup[0]])]
    path = path[:-1]
    for i in range(len(path) - 1):
        weight += G[path[i]][path[i + 1]]["weight"]
    return weight


def addNodes(G, nodes):
    for i in range(len(nodes)):
        a = nodes[i][0]
        b = nodes[i][1]
        c = nodes[i][2]
        G.add_edge(a, b, weight=-c)


def main():
    # Read the input file and get the list of test cases
    test_cases = read_input("input.txt")
    for i in range(len(test_cases)):
        if i == 192:
            source

        G = nx.DiGraph()
        addNodes(G, test_cases[i][2])
        a = G.nodes.get(1)
        if (a == None):
            addNodes(G, [[1, 1, -1]])
        source = 1

        try:
            # Check if there is a positive weighted cycle from 1 or from any node reachable from 1
            positive_cycle = False
            # for node in nx.descendants(G, source):
            # if i == 192:
            #     nx.simple_cycles()
            #     cycle = nx.find_cycle(G,source=source)
            cycle = nx.find_cycle(G, source=source,orientation="original")


            if get_weight_cycle(G, cycle) < 0:
                positive_cycle = True

            # If there is a positive weighted cycle, return -1 as a value instead
            if positive_cycle:
                # print(f"There is a positive weighted cycle in the graph: {cycle}")
                # print(f"The value of the heaviest path is -1")
                print("Unlimited!")
            else:
                # If there is no positive weighted cycle, find the heaviest path as before
                pathValues = (path for node in G.nodes() for path in nx.all_simple_paths(G, source, node))
                if len(list(pathValues)) == 0:
                    print(0)
                    continue
                heaviest_path = min((path for node in G.nodes() for path in nx.all_simple_paths(G, source, node)),
                                    key=lambda path: get_weight(G, path))
                # Print the result
                # print(f"There is no positive weighted cycle in the graph")
                # print(
                #     f"The heaviest path from {source} to any other node is {heaviest_path} with a weight of {get_weight(G,heaviest_path)}")
                value = get_weight(G, heaviest_path)
                if value > 0:
                    print(0)
                    continue
                print(-get_weight(G, heaviest_path))
        except nx.NetworkXNoCycle:
            # If there is no cycle at all, find the heaviest path as before
            pathValues = (path for node in G.nodes() for path in nx.all_simple_paths(G, source, node))
            if len(list(pathValues)) == 0:
                print(0)
                continue

            heaviest_path = min((path for node in G.nodes() for path in nx.all_simple_paths(G, source, node)),
                                key=lambda path: get_weight(G, path))
            # Print the result
            # print(f"There is no cycle in the graph")
            # print(
            #     f"The heaviest path from {source} to any other node is {heaviest_path} with a weight of {get_weight(G,heaviest_path)}")
            value = get_weight(G, heaviest_path)
            if value > 0:
                print(0)
                continue
            print(-get_weight(G, heaviest_path))
            continue


if __name__ == '__main__':
    main()
