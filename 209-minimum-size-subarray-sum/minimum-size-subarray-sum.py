class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        j = 0
        min_len = float("inf")
        curr_sum = 0

        while j < len(nums):
            curr_sum += nums[j]

            while curr_sum >= target:
                min_len = min(j-i+1, min_len)
                curr_sum -= nums[i]
                i+=1
            
            j+=1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
        