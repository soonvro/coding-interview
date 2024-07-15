from functools import cmp_to_key

def customCompare(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])

n = int(input())
inputs = [str(input()) for _ in range(n)]
inputs = list(set(inputs))
inputs.sort(key=cmp_to_key(customCompare))
for inputStr in inputs:
    print(inputStr)

