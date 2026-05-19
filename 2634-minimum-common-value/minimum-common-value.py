class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        arr = []

        for i in range(len(nums1)):
            if nums1[i] in s:
                arr.append(nums1[i])
        
        if len(arr) == 0:
            return -1
        else:
            return min(arr)