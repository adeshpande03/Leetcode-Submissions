class Solution:
    def surfaceArea(self, grid) -> int:
        length = len(grid)

        def behind(point):
            array = []
            i, j = point
            if length > i > 0:
                array.append(min((grid[i - 1][j], grid[i][j])))
            if j < length - 1:
                array.append(min((grid[i][j + 1], grid[i][j])))
            if i < length - 1:
                array.append(min((grid[i + 1][j], grid[i][j])))
            if length > j > 0:
                array.append(min((grid[i][j - 1], grid[i][j])))

            return array

        def tower_surface(height):
            return height * 6 - (height - 1) * 2 if height > 0 else 0

        surface = 0

        for i in range(length):
            for j in range(length):
                surface += tower_surface(grid[i][j]) - sum(behind((i, j)))

        return surface
