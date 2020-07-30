from typing import List
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 我的方法： DFS
# 其他方法： BFS 并查集


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_size = len(grid)
        if row_size == 0:
            return 0
        column_size = len(grid[0])
        visited = [([False] * column_size) for i in range (row_size)]

        def dfs(row, column):
            if 0 <= row < row_size and 0 <= column < column_size:
                if not visited[row][column]:
                    visited[row][column] = True
                    if(row+1) < row_size:
                        if grid[row + 1][column] == "1":
                            dfs(row + 1, column)
                    if (column+1) < column_size:
                        if grid[row][column + 1] == "1":
                            dfs(row, column + 1)
                    if (row-1) >= 0:
                        if grid[row - 1][column] == "1":
                            dfs(row - 1, column)
                    if (column-1) >= 0:
                        if grid[row][column - 1] == "1":
                            dfs(row, column - 1)

        count = 0
        for r in range(row_size):
            for c in range(column_size):
                if not visited[r][c] and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]

    print(s.numIslands(grid))
