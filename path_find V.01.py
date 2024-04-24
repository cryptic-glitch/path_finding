
def path_finding(grid, start, end, path=None):
    if path is None:
        path = [start]
    else:
        path.append(start)

    if start == end:
        return path

    if start not in grid:
        return None

    for node in grid[start]:
        if node not in path:
            newpath = path_finding(grid, node, end, path[:])
            if newpath:
                return newpath
    return None


# Define the matrix
matrix = [
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0]
]

# Convert the matrix into a grid representation
grid = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0: # if the value of the particular cell = 0, then we process it else we skip it
            if (i, j) not in grid: # if not already in the grid then add it
                grid[(i, j)] = []
            if i > 0 and matrix[i - 1][j] == 0:  # now we check 4 neighbors of the current cell
                grid[(i, j)].append((i - 1, j))
            if i < len(matrix) - 1 and matrix[i + 1][j] == 0:
                grid[(i, j)].append((i + 1, j))
            if j > 0 and matrix[i][j - 1] == 0:
                grid[(i, j)].append((i, j - 1))
            if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 0:
                grid[(i, j)].append((i, j + 1))

# Define start and end points
start_point = (7, 2)
end_point = (0, 4)

# Find the path
path = path_finding(grid, start_point, end_point)

# Print the path
if path:
    print("Congratulation the has been Path found:", path)
else:
    print("Go fuck your self")


# import time
#
#
# def path_finding(graph, start, end, path=None):
#     if path is None:
#         path = [start]
#     else:
#         path.append(start)
#
#     if start == end:
#         return path
#
#     if start not in graph:
#         return None
#
#     for node in graph[start]:
#         if node not in path:
#             newpath = path_finding(graph, node, end, path[:])
#             if newpath:
#                 return newpath
#     return None
#
#
# def create_graph(matrix):
#     graph = {}
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 if (i, j) not in graph:
#                     graph[(i, j)] = []
#                 if i > 0 and matrix[i - 1][j] == 0:
#                     graph[(i, j)].append((i - 1, j))
#                 if i < len(matrix) - 1 and matrix[i + 1][j] == 0:
#                     graph[(i, j)].append((i + 1, j))
#                 if j > 0 and matrix[i][j - 1] == 0:
#                     graph[(i, j)].append((i, j - 1))
#                 if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 0:
#                     graph[(i, j)].append((i, j + 1))
#     return graph
#
#
# def measure_time_complexity(matrix_size):
#     # Generate a matrix of given size
#     matrix = [[0] * matrix_size[1] for _ in range(matrix_size[0])]
#
#     # Start measuring time
#     start_time = time.time()
#
#     # Convert the matrix into a graph representation
#     graph = create_graph(matrix)
#
#     # Define start and end points
#     start_point = (matrix_size[0] - 1, 0)
#     end_point = (matrix_size[0] - 1, matrix_size[1] - 1)
#
#     # Find the path
#     path = path_finding(graph, start_point, end_point)
#
#     # End measuring time
#     end_time = time.time()
#
#     # Calculate the elapsed time
#     elapsed_time = end_time - start_time
#
#     return elapsed_time
#
#
# # Test different input sizes
# input_sizes = [(5, 5), (10, 10), (25, 25), (100,100)]  # Add more sizes if needed
#
# for size in input_sizes:
#     time_taken = measure_time_complexity(size)
#     print(f"Matrix size: {size}, Time taken: {time_taken:.6f} seconds")
#
