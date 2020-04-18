lst = [0] * 101
for i in map(int, input().split()):
    lst[i] += 1
srt = []
for i in range(len(lst)):
    srt.extend([i] * lst[i])
print(*srt)
