import time
import tracemalloc


# Generate all possible moves
def generate_moves(state):
    moves = []

    puzzle = list(state)

    # Find blank space (0)
    blank = puzzle.index(0)

    row = blank // 3
    col = blank % 3

    # UP
    if row > 0:
        new_puzzle = puzzle.copy()
        new_puzzle[blank], new_puzzle[blank - 3] = \
            new_puzzle[blank - 3], new_puzzle[blank]
        moves.append(tuple(new_puzzle))

    # DOWN
    if row < 2:
        new_puzzle = puzzle.copy()
        new_puzzle[blank], new_puzzle[blank + 3] = \
            new_puzzle[blank + 3], new_puzzle[blank]
        moves.append(tuple(new_puzzle))

    # LEFT
    if col > 0:
        new_puzzle = puzzle.copy()
        new_puzzle[blank], new_puzzle[blank - 1] = \
            new_puzzle[blank - 1], new_puzzle[blank]
        moves.append(tuple(new_puzzle))

    # RIGHT
    if col < 2:
        new_puzzle = puzzle.copy()
        new_puzzle[blank], new_puzzle[blank + 1] = \
            new_puzzle[blank + 1], new_puzzle[blank]
        moves.append(tuple(new_puzzle))

    return moves


# Depth Limited DFS
def depth_limited_search(state, goal_state, depth, visited):

    # Goal test
    if state == goal_state:
        return True

    # Depth limit reached
    if depth == 0:
        return False

    # Mark state as visited
    visited.add(state)

    # Generate possible moves
    next_states = generate_moves(state)

    for next_state in next_states:

        if next_state not in visited:

            if depth_limited_search(
                next_state,
                goal_state,
                depth - 1,
                visited
            ):
                return True

    return False


# Iterative Deepening DFS
def IDDFS(start_state, goal_state, max_depth):

    total_visited = set()

    # Start from depth 0
    for depth in range(max_depth + 1):

        print("\nSearching at depth:", depth)

        visited = set()

        found = depth_limited_search(
            start_state,
            goal_state,
            depth,
            visited
        )

        # Count visited states
        total_visited.update(visited)

        if found:
            return "Goal Found", len(total_visited), depth

    return "Goal Not Found", len(total_visited), max_depth


# Function to take 3x3 matrix input
def input_matrix(name):

    print(f"\nEnter {name} (3 x 3 matrix):")

    matrix = []

    for i in range(3):

        row = list(
            map(int, input(f"Enter row {i + 1}: ").split())
        )

        if len(row) != 3:
            print("Error: Enter exactly 3 numbers.")
            exit()

        matrix.append(row)

    # Convert matrix into tuple
    state = tuple(
        num for row in matrix for num in row
    )

    return state


# Function to display matrix
def display_matrix(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])


# ---------------- MAIN PROGRAM ----------------

print("Enter 0 for the blank space.")

# Input initial state
start = input_matrix("Initial State")

# Input goal state
goal = input_matrix("Goal State")


# Validate input
if set(start) != set(range(9)) or set(goal) != set(range(9)):

    print(
        "\nError: Matrix must contain numbers "
        "0 to 8 exactly once."
    )

    exit()


# Ask user for maximum depth
max_depth = int(
    input("\nEnter maximum depth limit: ")
)


# Display states
print("\nInitial State:")
display_matrix(start)

print("\nGoal State:")
display_matrix(goal)


# ---------------- PERFORMANCE MEASUREMENT ----------------

tracemalloc.start()

start_time = time.perf_counter()


# Run IDDFS
result, visited_count, solution_depth = IDDFS(
    start,
    goal,
    max_depth
)


end_time = time.perf_counter()


# Get memory usage
current_memory, peak_memory = tracemalloc.get_traced_memory()

tracemalloc.stop()


# ---------------- DISPLAY RESULT ----------------

print("\nResult:", result)

print("States Visited:", visited_count)

print("Solution Depth:", solution_depth)


print("\nTime Complexity Measurement:")

print(
    "Execution Time: {:.6f} seconds".format(
        end_time - start_time
    )
)


print("\nSpace Complexity Measurement:")

print(
    "Peak Memory Used: {:.2f} KB".format(
        peak_memory / 1024
    )
)


print("\nTheoretical Complexity:")

print("Time Complexity  : O(b^d)")

print("Space Complexity : O(bd)")

print(
    "where b = branching factor "
    "and d = depth limit"
)
