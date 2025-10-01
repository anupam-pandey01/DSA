class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 1
        curr_sum = nums[0]
        max_sum = nums[0]
        while(i < len(nums)):
            if(nums[i] > nums[i-1]):
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            max_sum = max(curr_sum, max_sum)
            i+=1
        return max_sum