### 1
![1 Задача](/tinkoff_summer_internship/images/1.jpg)
**Решение:**
```
n, m = map(int, input().split())
print(0 if n == m else n + m - 1)
```
### 2
![2 Задача](/tinkoff_summer_internship/images/2.jpg)
**Решение:**
```
s = input()
ss_start = s.find('@')
ss_end = len(s) - s[::-1].find('@')
print(s.replace(s[ss_start: ss_end], s[ss_start: ss_end][::-1]))
```
### 3
![3 Задача](/tinkoff_summer_internship/images/3.jpg)
**Решение:**
```
from typing import List


def find_split_index(distances: List[int], start: int, end: int) -> int:
    max_index = -1
    for i in range(start, end - 1):
        if distances[i] >= distances[max_index]:
            max_index = i
    return max_index

# assume that the min metric value is achieved when all analytics are split into the groups of 3 or less people
def split(distances: List[int], start: int, end: int):
    if (end - start < 4):  # if the group is small enough than compute metric
        global metric
        metric += distances[start] * (end - start)
    else:
        split_index = find_split_index(distances, start, end)
        split(distances, start, split_index + 1)
        split(distances, split_index + 1, end)


n = int(input())
a = sorted(map(int, input().split()))
distances = [a[i + 1] - a[i] for i in range(n-1)]

metric = 0
split(distances, 0, n)
print(metric)
```
### 4
![4 Задача](/tinkoff_summer_internship/images/4.jpg)
**Решение:**
```
import sys
n = int(input())
meetings = list(map(int, input().split()))

db = [meetings[i + 1] - meetings[i] for i in range(len(meetings))] #meetings between mettings
changes = [i + 1 for i in range(len(db) - 1) if db[i] - db[i + 1] != 0]

if len(changes) > 2:
    dist = changes[3] - changes[1]
    for i in range(len(changes) / 2):
        if (dist != changes[i + 2] - changes[i]):
            print('kukuha')
            sys.exit()
    t = (meetings[changes[3]] - meetings[changes[1]]) / (changes[3] - changes[1])
elif len(changes) == 0:
    t = meetings[2] - meetings[1]
else:
    t = meetings[changes[2]] - meetings[1]

print(t - 0.5, t + 0.5)
```
### 5
![5 Задача](/tinkoff_summer_internship/images/5.jpg)
**Решение:**
```
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
```
### 6
![6 Задача](/tinkoff_summer_internship/images/6.jpg)
**Решение:**
```
x, y = map(float, input().split())
is_land_successfull  = (0.5 * x**2 + y**2 < 1) and (y < 0.5 * abs(x) + 0.5) and \
                       ((x - 0.5)**2 + y**2 > 0.3) and ((x + 0.5)**2 + y**2 > 0.3) 
print('YES' if is_land_successfull else 'NO')
```
### 7
![7 Задача](/tinkoff_summer_internship/images/7.jpg)
**Решение:**
```
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
```
