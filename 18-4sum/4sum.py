class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue
                
                s = j+1
                w = n-1
                while(s < w):
                    total = nums[i] + nums[j] + nums[s] + nums[w]

                    if total == target:
                        result.append([nums[i], nums[j], nums[s], nums[w]])
                        s+=1
                        w-=1
                        #skip duplicate of s 
                        while s < w and nums[s] == nums[s-1]:
                            s += 1
                        
                        while s < w and nums[w] == nums[w+1]:
                            w -= 1
                        

                    elif total > target:
                        w -= 1
                    else:
                        s += 1
        return result