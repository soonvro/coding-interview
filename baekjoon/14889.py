# TAG: DFS, brute_force
n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = int(1e9)

def dfs(member, cnt):
    global result
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] and i != j:
                    start += stats[i][j]
                elif not visited[i] and not visited[j] and i != j:
                    link += stats[i][j]
        result = min(result, abs(start - link))
        return

    for i in range(member, n):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0, 0)
print(result)
