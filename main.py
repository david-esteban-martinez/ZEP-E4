# Define a function to read the input file and return a list of test cases
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


# Define a function to find the maximum procrastination and the path for a given test case
def max_procrastination_and_path(test_case):
    # Unpack the test case into N, M and decisions
    N, M, decisions = test_case
    # Initialize a dictionary to store the maximum procrastination for each life-point
    procrastination = {i: 0 for i in range(1, N + 1)}
    # Initialize a dictionary to store the previous life-point for each life-point in the optimal path
    previous = {i: None for i in range(1, N + 1)}
    # Initialize a flag to indicate if there is a negative cycle in the graph
    negative_cycle = False
    # Repeat the following loop N times
    for _ in range(N):
        # Initialize a variable to track if any procrastination value is updated in this iteration
        updated = False
        # Loop through all the decisions
        for A, B, F in decisions:
            # If the procrastination value at B can be increased by going from A to B
            if procrastination[B] < procrastination[A] + F:
                # Update the procrastination value at B
                procrastination[B] = procrastination[A] + F
                # Update the previous life-point at B
                previous[B] = A
                # Set the updated flag to True
                updated = True
        # If no procrastination value is updated in this iteration
        if not updated:
            # Break out of the loop
            break
        # If this is the last iteration and some procrastination value is still updated
        if _ == N - 1 and updated:
            # Set the negative cycle flag to True
            negative_cycle = True

    # Check if life-point N is reachable from life-point 1 by using a breadth-first search algorithm
    reachable = False
    visited = set()  # A set to store the visited life-points
    queue = [1]  # A queue to store the life-points to be explored next
    while queue:  # While the queue is not empty
        current = queue.pop(0)  # Pop the first life-point from the queue
        visited.add(current)  # Mark it as visited
        if current == N:  # If it is equal to N
            reachable = True  # Set the reachable flag to True and break out of the loop
            break
        for A, B, F in decisions:  # Loop through all the decisions
            if A == current and B not in visited:  # If there is a decision from current to another unvisited life-point
                queue.append(B)  # Append that life-point to the queue

    # If there is a negative cycle in the graph or life-point N is not reachable from life-point 1
    if negative_cycle or not reachable:
        # Return "Unlimited!" or "0" as the answer respectively
        return "Unlimited!" if negative_cycle else "0", None
    else:
        # Return the maximum procrastination value at life-point N as the answer and reconstruct the path by using previous dictionary
        path = [N]
        current = N
        while previous[current]:
            path.append(previous[current])
            current = previous[current]
        path.reverse()
        return procrastination[N], path


# Main function to run the program
# Main function to run the program
def main():
  # Read the input file and get the list of test cases
  test_cases = read_input("input.txt")
  # Loop through each test case and print the output
  for i, test_case in enumerate(test_cases):
    max_procrastination, path = max_procrastination_and_path(test_case)
    print(f"Test case {i + 1}:")
    print(f"Maximum procrastination: {max_procrastination}")
    if path:
      print(f"Path: {' -> '.join(map(str, path))}")
    print()

if __name__ == '__main__':
    main()