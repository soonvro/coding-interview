def dfs(node):
    global ret
    if node == remove:
        return
    if len(tree[node]) == 0 or (len(tree[node]) == 1 and tree[node][0] == remove):
        ret += 1
        return
    for child in tree[node]:
        dfs(child)

n = int(input())
parents = list(map(int, input().split()))
remove = int(input())
ret = 0

root = -1
tree = dict()
for i in range(n):
    tree[i] = []
for i in range(n):
    if parents[i] != -1:
        tree[parents[i]].append(i)
    else:
        root = i

dfs(root)
print(ret)
