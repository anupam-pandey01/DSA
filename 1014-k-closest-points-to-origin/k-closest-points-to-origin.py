import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for i in range(k):
            x, y = points[i]
            d = math.sqrt(((0 - x)**2) + ((0 - y)**2))
            heapq.heappush(heap, (-d, [x, y]))
        
        
        for j in range(k, len(points)):
            x, y = points[j]
            d = math.sqrt(((0 - x)**2) + ((0 - y)**2))

            if d <= -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-d, [x, y]))
        
        for i in range(len(heap)):
            result.append(heap[i][1])
        
        return result
