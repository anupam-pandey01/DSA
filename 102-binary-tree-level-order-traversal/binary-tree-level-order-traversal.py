from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque([])
        queue.append(root)

        while len(queue) != 0:
            level_val = []
            level_len = len(queue)

            for i in range(level_len):
                e = queue.popleft()
                level_val.append(e.val)

                if e.left:
                    queue.append(e.left)
                
                if e.right:
                    queue.append(e.right)
            result.append(level_val)
        
        return result