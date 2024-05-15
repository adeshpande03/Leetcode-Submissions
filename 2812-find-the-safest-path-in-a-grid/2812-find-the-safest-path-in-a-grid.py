import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        if grid[0][0] or grid[n-1][m-1]:
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i,j])
                    vis[i][j] = 1
        cnt = 0
        while len(q) != 0:
            size = len(q)
            for k in range(size):
                node = q.popleft()
                grid[node[0]][node[1]] = cnt
                for i in range(4):
                    nr = node[0] + dr[i]
                    nc = node[1] + dc[i]
                    if nr >= 0 and nr < n and nc >= 0 and nc < m and vis[nr][nc] == 0 and grid[nr][nc] == 0:
                        q.append([nr,nc])
                        vis[nr][nc] = 1
                        # grid[nr][nc] = cnt
                
            cnt += 1
        
        
        
        q = []
        heapq.heappush(q,[-1*grid[0][0],0,0])
        dist = [[0 for i in range(m)] for j in range(n)]
        while len(q) != 0:
            # node = q.popleft()
            node = heapq.heappop(q)
            dis = -1*node[0]
            r = node[1]
            c = node[2]
            if r == n-1 and c == m-1:
                return dis
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= 0 and nr < n and nc >= 0 and nc < m:
                    mini = min(dis,grid[nr][nc])
                    if mini > dist[nr][nc]:
                        # q.append([mini,nr,nc])
                        heapq.heappush(q,[-1*mini,nr,nc])
                        dist[nr][nc] = mini
                    
        return dist[n-1][m-1]


            
        
                    
        
           
            
        