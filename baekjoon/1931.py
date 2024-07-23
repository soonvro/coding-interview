from operator import itemgetter

n = int(input())
plans = [tuple(map(int, input().split())) for _ in range(n)]

plans.sort(key=itemgetter(1, 0))
ret = 0

end = 0
for plan in plans:
    start = plan[0]
    if start < end:
        continue
    ret += 1
    end = plan[1]

print(ret)
