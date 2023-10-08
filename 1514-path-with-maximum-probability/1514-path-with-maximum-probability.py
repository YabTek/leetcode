class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)

        for i, (a, b) in enumerate(edges):
            graph[a].append((b, -math.log(succProb[i])))
            graph[b].append((a, -math.log(succProb[i])))

        dist = {node : inf for node in range(n)}
        dist[start_node] = 0

        heap = [(0, start_node)]

        while heap:
            prob, node = heapq.heappop(heap)
            if node == end_node:
                return math.exp(-prob)  
            
            if prob > dist[node]:
                continue  

            for neighbour, weight in graph[node]:
                new_prob = prob + weight
                if new_prob < dist[neighbour]:
                    dist[neighbour] = new_prob
                    heapq.heappush(heap, (new_prob, neighbour))

        return 0  



