Easy graph traversal problem:
"Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
​
Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise."
​
python
class Solution:
def isPathCrossing(self, path: str) -> bool:
x, y = 0, 0
seen = set()
seen.add((x, y))
d = {"N":(1, 0),"E":(0, 1),"S":(-1, 0),"W":(0, -1)}
for i in path:
x += d[i][1]
y += d[i][0]
if (x, y) in seen:
return True
seen.add((x, y))
return False