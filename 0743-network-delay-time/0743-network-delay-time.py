class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        
        for a, b, c in times:
            graph[a].append((b, c))
            
        time = {node: inf for node in range(1, n+1)}
        time[k] = 0
        heap = [(0, k)]
        
        while heap:
            cur_time, cur_node = heapq.heappop(heap)
            
            if cur_time > time[cur_node]:
                continue
                
            for neighbour, weight in graph[cur_node]:
                new_time = cur_time + weight
                if new_time < time[neighbour]:
                    time[neighbour] = new_time
                    heapq.heappush(heap, (new_time, neighbour))
                    
        ans = max(time.values())
        
        if ans == inf:
            return -1
        return ans