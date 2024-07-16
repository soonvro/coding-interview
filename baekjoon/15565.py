# for 리스트 탐색하며, 1을 찾는다.
#   1을 찾으면, 그 인덱스를 queue에 넣는다.
#   queue의 사이즈가 k와 같아지면, queue의 가장 뒤에 있는 인덱스와 현재 인덱스의 차이를 구하고, pop한다.
#   ret = min(ret, 차이)

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ret = float('inf')

queue = deque()
for i in range(n):
    if arr[i] == 1:
        queue.append(i)
        if len(queue) == k:
            idxOfHead = queue.popleft()
            ret = min(ret, i - idxOfHead + 1)

if ret == float('inf'):
    print(-1)
else:
    print(ret)
