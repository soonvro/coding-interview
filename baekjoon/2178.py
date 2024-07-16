'''
=== 조건 ===
1. 미로의 크기는 N x M 이다.
2. 미로는 빈 공간과 벽으로 이루어져 있으며, 빈 공간은 1, 벽은 0으로 표시된다.
3. 미로의 시작 위치는 (1, 1)이고, 출구는 (N, M)이다.
4. 한 번에 한 칸씩 이동할 수 있으며, 이동할 수 있는 칸은 상하좌우로 인접한 빈 공간이다.
5. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
6. (2 ≤ N, M ≤ 100)

=== 생각 ===
1. BFS, Bruteforce, Backtracking 을 이용하여 풀 수 있을 것 같다.
2. 구현을 위해 지나왔던 길을 표시해야 한다. -> 최단거리를 구하는 문제이기 때문에

=== 풀이 ===
n, m: 입력받기
miro: 미로 입력받기

'''
from collections import deque

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if miro[nx][ny] == 0:
            continue
        if miro[nx][ny] == 1:
            miro[nx][ny] = miro[x][y] + 1
            queue.append((nx, ny))

print(miro[n - 1][m - 1])
