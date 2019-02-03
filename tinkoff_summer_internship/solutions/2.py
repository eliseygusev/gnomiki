s = input()
ss_start = s.find('@')
ss_end = len(s) - s[::-1].find('@')
print(s.replace(s[ss_start: ss_end], s[ss_start: ss_end][::-1]))
