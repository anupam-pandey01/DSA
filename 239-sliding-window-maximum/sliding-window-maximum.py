from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []

        for j in range(len(nums)):
            # 1. Remove indices outside the current window
            while dq and dq[0] <= j - k:
                dq.popleft()

            # 2. Remove smaller or equal values from the back
            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()

            # 3. Add the current index
            dq.append(j)

            # 4. Record the maximum when the window is full
            if j >= k - 1:
                result.append(nums[dq[0]])

        return result