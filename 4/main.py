st = (str(input())).split()
print(*[st[:i].count(st[i]) for i in range(len(st))],end = "")

