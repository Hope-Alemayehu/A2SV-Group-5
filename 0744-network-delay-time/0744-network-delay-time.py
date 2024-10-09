class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for start, end, weight in times:
            graph[start].append((end, weight))
        

        distance = {node: float("inf") for node in range(1,n+1)}
        distance[k] = 0

        heap = [(0, k)]
        while heap:

            node_val, node = heap.pop()

            for neighbour, weight in graph[node]:
                if node_val + weight < distance[neighbour]:
                    distance[neighbour] = node_val + weight
                    heapq.heappush(heap,(distance[neighbour], neighbour))
            
        ans = max(distance.values())
        return ans if ans != float("inf") else -1