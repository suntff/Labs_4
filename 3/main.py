a = []
print("Введите n:")
n = int(input())
i = 0
while i<n:
    a.append(str(input()))
    if len(set(a))<len(a):
        print("OK")
        a = a[:-1]
    else:
        print("REPEAT")
        i+=1
