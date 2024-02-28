from typing import List, Dict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        distances = {i: float('inf') for i in range(n)}
        distances[src] = 0
        
        heap = [(0, src)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            if node in graph:
                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
        
        return {i: dist if dist != float('inf') else -1 for i, dist in distances.items()}

# Example usage
n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0
sol = Solution()
print(sol.shortestPath(n, edges, src))

""" 
Implement Dijkstra's shortest path algorithm.

Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
src - the source vertex from which to start the algorithm, where (0 <= src < n).
Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.
 """