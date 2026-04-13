from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        target_img = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while len(queue) != 0:
            total_len = len(queue)
            
            for _ in range(total_len):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i = i + dx
                    new_j = j + dy

                    if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                    
                    if image[new_i][new_j] == color or image[new_i][new_j] != target_img:
                        continue
                    
                    image[new_i][new_j] = color
                    queue.append((new_i, new_j))
                
        return image
