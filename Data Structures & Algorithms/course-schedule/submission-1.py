from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = []
        adjList, inDegree = self.helper(numCourses, prerequisites)

        # Push nodes with 0 in-degree into the stack
        for i in range(numCourses):
            if inDegree[i] == 0:
                stack.append(i)

        count = 0
        while stack:
            current = stack.pop()
            count += 1
            for neighbor in adjList[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    stack.append(neighbor)

        return count == numCourses

    def helper(self, n: int, prereq: List[List[int]]):
        adjList = [[] for _ in range(n)]
        inDegree = [0 for _ in range(n)]

        for course in prereq:
            toTake, firstTake = course  # Unpacked correctly
            adjList[firstTake].append(toTake)
            inDegree[toTake] += 1

        return adjList, inDegree
