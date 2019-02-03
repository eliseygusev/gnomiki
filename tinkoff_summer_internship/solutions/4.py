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
