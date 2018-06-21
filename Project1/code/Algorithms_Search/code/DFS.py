def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)