class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def allsubset(nums, op):
            if(len(nums) == 0):
                ans.append(op)
                return

            op1 = op.copy()
            op2 = op.copy()

            op2.append(nums[0])
            
            allsubset(nums[1:], op1)
            allsubset(nums[1:], op2)

        allsubset(nums, [])
            
        return ans
