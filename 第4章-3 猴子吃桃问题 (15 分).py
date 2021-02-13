def dfs(n):
    if n == 1:
        return 1
    else:
        return (dfs(n - 1) + 1) * 2

n = int(input())
print(dfs(n))