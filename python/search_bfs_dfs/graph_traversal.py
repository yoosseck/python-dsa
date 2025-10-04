class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_edge(self, u, v):
        """Add an edge from u to v (undirected)."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # remove if directed

    def bfs(self, start):
        """Breadth-First Search (BFS) without deque"""
        if start not in self.graph:
            return []
        visited = {start}
        queue = [start]  # list used as queue
        result = []

        while queue:
            node = queue.pop(0)   # remove from front (O(n))
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        """Depth-First Search (DFS) iterative"""
        if start not in self.graph:
            return []
        visited = {start}
        stack = [start]
        result = []

        while stack:
            node = stack.pop()  # pop from end
            result.append(node)
            for neighbor in reversed(self.graph[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return result

    def dfs_recursive(self, node, visited=None):
        """Recursive DFS"""
        if visited is None:
            visited = set()
        visited.add(node)
        result = [node]
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        return result


# Example usage:
g = Graph()
edges = [
    ("A", "B"), ("A", "C"),
    ("B", "D"), ("B", "E"),
    ("C", "F"), ("E", "F")
]

for u, v in edges:
    g.add_edge(u, v)

print("BFS:", g.bfs("A"))
print("DFS (iterative):", g.dfs("A"))
print("DFS (recursive):", g.dfs_recursive("A"))
