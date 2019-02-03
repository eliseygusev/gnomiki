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
