from collections import deque

class Solution(object):
       
    def validPath(self, n, edges, source, destination):

        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b in edges:

            graph[a].append(b)

            graph[b].append(a)
        
        queue = deque()

        visited = set()

        queue.append(source)

        visited.add(source)

        while queue:
                node = queue.popleft()

                if node == destination:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                
                        visited.add(neighbor)

                        queue.append(neighbor)
            
        return False
        


       
