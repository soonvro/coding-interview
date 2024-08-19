# TAG: brute_force, dfs

n = int(input())
operands = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ret = int(-1e9)
min_ret = int(1e9)

def dfs(add, sub, mul, div, ret, depth):
    global max_ret, min_ret
    
    if depth == (n - 1):
        max_ret = max(max_ret, ret)
        min_ret = min(min_ret, ret)
        return

    if add:
        dfs(add - 1, sub, mul, div, ret + operands[depth + 1], depth + 1)
    if sub:
        dfs(add, sub - 1, mul, div, ret - operands[depth + 1], depth + 1)
    if mul:
        dfs(add, sub, mul - 1, div, ret * operands[depth + 1], depth + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(ret / operands[depth + 1]), depth + 1)

dfs(add, sub, mul, div, operands[0], 0)
print(max_ret)
print(min_ret)
