class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x,y,visited):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]!= 1 or visited[x][y]:
                return
            visited[x][y]=True
            dfs(x-1,y,visited)
            dfs(x+1,y,visited)
            dfs(x,y-1,visited)
            dfs(x,y+1,visited)
        def count_islands():
            visited =[[False] * n for _ in range(m)]
            count=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and not visited[i][j]:
                        dfs(i,j,visited)
                        count +=1
            return count

        def is_disconnected():
            return count_islands() !=1

        m,n =len(grid),len(grid[0])
        if is_disconnected():
            return 0
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if is_disconnected():
                        return 1
                    grid[i][j]=1  
        return 2