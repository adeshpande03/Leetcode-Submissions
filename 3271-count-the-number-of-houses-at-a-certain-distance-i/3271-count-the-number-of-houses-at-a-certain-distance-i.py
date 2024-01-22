class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0] * n
        adjacency_list = defaultdict(list)
        for i in range(1, n):
            adjacency_list[i].append(i + 1)
            adjacency_list[i + 1].append(i)
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

        def bfs(i):
            q = deque()
            visit = set()
            q.append((i, 0))
            visit.add(i)
            while q:
                i, dist = q.popleft()
                if dist > 0:
                    res[dist - 1] += 1
                for nei in adjacency_list[i]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, dist + 1))

        for i in range(1, n + 1):
            bfs(i)

        return res
