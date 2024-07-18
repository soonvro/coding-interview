from collections import deque

r, c = map(int, input().split())
miro = [list(input()) for _ in range(r)]

visited = [[-1] * c for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

queue = deque()

pos_hedgehog = ()
pos_dest = ()
for _y in range(r):
    for _x in range(c):
        if miro[_y][_x] == 'D':
            pos_dest = (_y, _x)
        elif miro[_y][_x] == 'S':
            pos_hedgehog = (_y, _x)
            visited[_y][_x] = 0
        elif miro[_y][_x] == '*':
            queue.append((_y, _x))
queue.append(pos_hedgehog)

while queue:
    y, x = queue.popleft()
    cur = miro[y][x]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if visited[ny][nx] != -1:
            continue
        if miro[ny][nx] in ['*', 'X']:
            continue
        if cur == '*' and miro[ny][nx] == 'D':
            continue

        if cur == 'S':
            if miro[ny][nx] == 'D':
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1

        miro[ny][nx] = cur
        queue.append((ny, nx))
    else:
        continue
    break
else:
    print("KAKTUS")
