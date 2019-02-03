def dfs(key, tree, result):
    if key in tree:
        for c in tree[key]:
            result[c] = result[key] + 1
            dfs(c, tree, result)


n = int(input())
tree = {}
result = {'X': 0}

for i in range(n - 1):
    s = input().split()
    if not (s[1] in tree):
        tree[s[1]] = []
    tree[s[1]].append(s[0])

dfs('X', tree, result)
for i in sorted(result.keys()):
    print(i, result[i])
