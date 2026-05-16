from collections import deque

def bfs(graph, start_node):
    # Keep track of visited nodes to avoid cycles
    visited = set()
    
    # Create a queue for BFS and enqueue the starting node
    queue = deque([start_node])
    
    # Mark the starting node as visited
    visited.add(start_node)
    
    print("BFS Traversal Order:")
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the front of the queue
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent node hasn't been visited, mark it visited and enqueue it
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print() # For a clean newline at the end

# --- Example Usage ---

# Representing the graph using an Adjacency List
# 
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS starting from node 'A'
bfs(example_graph, 'A')