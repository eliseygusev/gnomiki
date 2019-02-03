n, m = map(int, input().split())
queries = 0
available_for_work = [True for i in range(n)]
skill_matrix = [list(map(int, input().split())) for i in range(m)]
s = [sum(i) for i in zip(*skill_matrix)]

for i in range(m):
    index = s.index(min(s))
    for j in range(n):
        if (available_for_work[j]) and skill_matrix[j][index] == 1:
            available_for_work[j] = False
            queries += 1
            break
    s[index] = 1000

print(queries)
