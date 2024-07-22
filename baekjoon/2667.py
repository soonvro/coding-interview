def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if miro[nx][ny] == 0 or visited[nx][ny] == 1:
            continue
        dfs(nx, ny)

n = int(input())
miro = [list(map(int, input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
result = []

for _y in range(n):
    for _x in range(n):
        if miro[_y][_x] == 1 and visited[_y][_x] == 0:
            cnt = 0
            dfs(_y, _x)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)
