"""
This question is given input 1 and 0, to get how many Islands is over here
solution: bfs(queue), dfs(stack)
"""
from collections import deque


def numIslands(grid):
    if not grid:
        return
    rows = len(grid)
    cols = len(grid[0])
    ans = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                queue = deque([(row, col)])
                grid[row][col] = "2"
                while queue:
                    d_row, d_col = queue.popleft()
                    for r, c in (0, 1), (-1, 0), (0, -1), (1, 0):
                        new_row, new_col = d_row + r, d_col + c
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = "2"
                ans += 1
    return ans


if __name__ == '__main__':
    input_1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(input_1))



# when do use visitied,when do just modify the original ele?


