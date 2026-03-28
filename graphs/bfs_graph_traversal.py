from collections import deque

def bfs_graph(graph, start_node):
    # visited: 訪問済みリスト
    visited = []
    # queue: 探索待ちリスト (Pythonではdequeが効率的ですが、標準リスト pop(0) でも可)
    queue = deque([start_node])
    
    print(f"--- BFS Start: {start_node} ---")
    
    while queue:
        # VSCodeのブレークポイントをここに置くと、毎ステップのqueueの状態がわかります
        current = queue.popleft()
        
        if current not in visited:
            visited.append(current)
            print(f"Visiting: {current} | Visited so far: {visited}")
            
            # 未訪問の隣接ノードを抽出
            neighbors = [n for n in graph[current] if n not in visited]
            queue.extend(neighbors)
            
    return visited

# テスト用グラフ（隣接リスト）
graph_data = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

if __name__ == "__main__":
    result = bfs_graph(graph_data, 'A')
    print(f"Final Path: {result}")