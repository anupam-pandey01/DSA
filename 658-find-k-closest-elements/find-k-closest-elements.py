import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        result = []

        for i in range(k):
            diff = abs(arr[i] - x)
            heapq.heappush(heap, (-diff, arr[i]))

        for j in range(k, len(arr)):
            diff = abs(arr[j] - x)

            if diff < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-diff, arr[j]))

        while heap:
            result.append(heapq.heappop(heap)[1])

        return sorted(result)