from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_adj_list(numCourses, prerequisites)

        for vertex in range(numCourses):
            if self.bfs(vertex, graph):
                return False
        return True

    def build_adj_list(self, n, prereq):
        adjList = [[] for _ in range(n)]
        for toTake, firstTake in prereq:
            adjList[firstTake].append(toTake)
        return adjList

    def bfs(self, start, graph):
        queue = deque()
        visited = set()

        for neighbor in graph[start]:
            queue.append(neighbor)

        while queue:
            curr = queue.popleft()
            if curr == start:
                return True  # cycle detected

            if curr in visited:
                continue
            visited.add(curr)

            for neighbor in graph[curr]:
                queue.append(neighbor)

        return False
