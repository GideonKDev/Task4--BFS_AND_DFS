def dfs_recursive(graph, current_node, visited=None):
    # Initialize the visited set on the first call
    if visited is None:
        visited = set()
        print("DFS Order of Traversal:")
        
    # Mark the current node as visited
    visited.add(current_node)
    print(current_node, end=" ")
    
    # Recur for all the neighbors that haven't been visited yet
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# --- Example Graph Setup ---
example_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run the algorithm starting from node 'A'
dfs_recursive(example_graph, 'A')
print() # For a clean newline