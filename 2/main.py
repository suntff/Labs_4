n1,n2 = int(input()),int(input())
m1 = set(int(input()) for i in range(n1))
m2 = set(int(input()) for i in range(n2))
c = 0
for i,val1 in enumerate(m1):
    for j,val2 in enumerate(m2):
        if val1==val2:
            c+=1
            break
    if c==len(m1):
        print("True")
        break
if c!=len(m1):
    print("False")
