class Solution(object):
    def majorityElement(self, nums):
        ans=nums[0]
        count=0
        for i in range(len(nums)):
            if(count == 0):
                ans = nums[i]
            if(ans != nums[i]):
                count-=1
            else:
                count+=1
        return ans
    
            
                
        