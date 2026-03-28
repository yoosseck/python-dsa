def dfs_graph_traversal(graph, current, visited=None):
    if visited is None:
        visited = []
    
    # VSCodeのブレークポイントをここに置く
    # コールスタックを見ることで「今、どの分岐の深くにいるか」がわかります
    visited.append(current)
    print(f"DFS Depth: {len(visited)} | Visiting: {current}")
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs_graph_traversal(graph, neighbor, visited)
            
    return visited

# テスト用グラフ
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

if __name__ == "__main__":
    print(f"--- DFS Start ---")
    result = dfs_graph_traversal(graph_data, 'A')
    print(f"Final Path: {result}")