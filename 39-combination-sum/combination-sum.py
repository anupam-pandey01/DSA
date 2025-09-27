class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, tar, comb):
            if(tar == 0):
                ans.append(comb.copy())
                return
            
            if(idx >= len(candidates) or tar < 0):
                return
            
            comb.append(candidates[idx])
            backtrack(idx, tar - candidates[idx], comb)

            comb.pop()
            backtrack(idx+1, tar, comb)
        
        backtrack(0, target, [])
        return ans
