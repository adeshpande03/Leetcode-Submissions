class Solution:
    def maximumImportance(self, n, roads):
        freq = [0] * n

        # Count frequencies (degree) of each node
        for road in roads:
            freq[road[0]] += 1
            freq[road[1]] += 1

        # Sort the frequency array
        freq.sort()

        ans = 0
        for i in range(n):
            ans += (i + 1) * freq[i]

        return ans