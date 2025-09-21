class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        curr_sum = 0
        max_sum = nums[0]

        while(j < len(nums)):
            curr_sum += nums[j]
            if(curr_sum > max_sum):
                max_sum = curr_sum
            
            if(curr_sum < 0):
                curr_sum = 0
                i+=1
            j+=1
        return max_sum
