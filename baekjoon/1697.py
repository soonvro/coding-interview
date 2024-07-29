# TAG: BFS

from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001  # save visited & depth in one list
queue = deque([n])
visited[n] = 0
ret = 0

while queue:
    curN = queue.popleft()
    if curN == k:
        ret = visited[curN]
        break
    for i in [curN-1, curN+1, curN*2]:
        if 0 <= i <= 100000 and visited[i] == -1:
            visited[i] = visited[curN] + 1
            queue.append(i)

print(ret)
