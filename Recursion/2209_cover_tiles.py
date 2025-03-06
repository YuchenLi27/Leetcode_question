class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(map(int, floor))  # have every singel tiles as a string

        dp = [[-1] * (numCarpets + 1) for _ in range(len(floor) + 1)]
        return self.helper(0, numCarpets, carpetLen, floor, dp)

    def helper(self, cur, stack, cover, floor, dp):
        if cur >= len(floor): return 0
        if dp[cur][stack] != -1:
            return dp[cur][stack]

        # if stack == 0: return sum(floor[cur:])
        # we dont cover current tile
        res = self.helper(cur + 1, stack, cover, floor, dp) + floor[cur]
        # + floor[cur] : current position is NOT covered,
        # so the fianl result, the num of tailes taht not covered will be added

        if stack > 0:
            max_cover = min(cover, len(floor) - cur)

            for remaina_taile_ele in range(1, max_cover + 1):
                res = min(res, self.helper(cur + remaina_taile_ele, stack - 1, cover, floor, dp))
        dp[cur][stack] = res
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumWhiteTiles("10110101", 2, 2))