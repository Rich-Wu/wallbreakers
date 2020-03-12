from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, req in prerequisites:
            graph[course].append(req)
        visit = [0 for _ in range(numCourses)]
        res = []
        def dfs(i):
            if visit[i] == -1:
                return []
            visit[i] = -1
            for j in graph[i]:
                if visit[j] == 0:
                    dfs(j)
                elif visit[j] == -1:
                    return []
            visit[i] = 1
            res.append(i)
        for course in range(numCourses):
            if visit[course] == 0:
                dfs(course)
            elif visit[course] == -1:
                return []
        return res