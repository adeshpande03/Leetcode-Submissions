class Solution:
    found = False
    start_of_cycle = -1
    cycle = {}
    def clear(self):
        self.found = False
        self.start_of_cycle = -1
        self.cycle.clear()

    def find_cycle(self, adj_list, node, visited, prev_node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.find_cycle(adj_list, neighbor, visited, node)
                if self.found:
                    self.cycle[neighbor] = 1
                    if self.start_of_cycle == neighbor:
                        self.found = False
                    return
            elif visited[neighbor] and prev_node != neighbor:
                self.start_of_cycle = neighbor
                self.cycle[neighbor] = 1
                self.found = True
                return
    
    def bfs(self, ans, n, adj_list, node):
        q = []
        q.append((node, 0))
        ans[node] = 0
        visited = [False for _ in range(n)]
        visited[node] = True
        while q:
            (cur, dist) = q.pop(0)
            ans[cur] = dist
            for neighbor in adj_list[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if neighbor in self.cycle:
                        q.append((neighbor, dist))
                    else:
                        q.append((neighbor, dist + 1))

    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        self.clear()
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited = [False for _ in range(n)]
        self.find_cycle(adj_list, 0, visited, -1)
        ans = [0 for _ in range(n)]
        self.bfs(ans, n, adj_list, self.start_of_cycle)
        return ans

        