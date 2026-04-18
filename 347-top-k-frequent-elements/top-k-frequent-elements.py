import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] = freq[nums[i]] + 1
            else:
                freq[nums[i]] = 1
            
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result