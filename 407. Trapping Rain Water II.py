# https://leetcode.com/problems/trapping-rain-water-ii/description/

import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Add all the boundary cells to the min-heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water_trapped = 0
        max_height = 0
        
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            max_height = max(max_height, height)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Water trapped at this cell is the difference between max_height and the cell's height
                    if heightMap[nx][ny] < max_height:
                        water_trapped += max_height - heightMap[nx][ny]
                    heapq.heappush(min_heap, (heightMap[nx][ny], nx, ny))
        
        return water_trapped