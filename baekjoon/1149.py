# TAG: DP, dynamic programming

N_COLORS = 3
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * N_COLORS for _ in range(n)]
dp[0] = costs[0]

for i in range(1, n):
    for c in range(N_COLORS):
        dp[i][c] = min(dp[i - 1][_j] for _j in range(N_COLORS) if _j != c) + costs[i][c]

print(min(dp[n - 1]))
