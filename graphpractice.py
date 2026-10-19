from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

def most_connected(graph):
    best_node = None
    best_count = 0
    for key in graph:
        if len(graph[key]) > best_count:
            best_count = len(graph[key])
            best_node = key
    return best_node
def bfs(graph,start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return result
def dfs(graph,node,visited,result):
    visited.add(node)
    result.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited,result)
    return result



print(most_connected(graph))  # expected: D
print(bfs(graph, "A"))  # expected: ['A', 'B', 'C', 'D', 'E']
print(bfs(graph, "E"))  # expected: ['E', 'D', 'B', 'C', 'A']
print(dfs(graph, "A", set(), []))  # expected: ['A', 'B', 'D', 'C', 'E']
print(dfs(graph, "E", set(), []))