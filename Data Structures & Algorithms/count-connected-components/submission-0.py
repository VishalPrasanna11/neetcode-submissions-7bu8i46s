class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = build_adj(n,edges)

        visited = {}

        count = 0

        for vertex in range(n):
            if vertex not in visited:
                count += 1
                dfs(graph,vertex,visited)

        return count

def build_adj(n,edges):
    adj_list = [[] for _ in range(n)]

    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    return adj_list


def dfs(graph,vertex, visited):

    visited[vertex] = True

    neighbors = graph[vertex]

    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)



        