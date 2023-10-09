class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
       
        distance = [float('inf')] * n
        distance[src] = 0
        
        for _ in range(k + 1):
            new_dist = list(distance)
            
            for a, b, c in flights:
                if distance[a] + c < new_dist[b]:
                    new_dist[b] = distance[a] + c
            
            distance = new_dist
        
        return distance[dst] if distance[dst] != float('inf') else -1