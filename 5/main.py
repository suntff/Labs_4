s = [[253, "Карандаш" ,3],  [25, "Ручка" ,2],[253, "Пенал" ,5],[2, "Принтер" ,1],[25, "Монитор" ,2]]
dt = {s[i][0]:[] for i in range(len(s))}
for i in range(len(s)):
    dt[s[i][0]]+=[s[i][1:3]]

for i in dt:
    print(f"id покупателя: {i}",",","покупки:",end = " ",sep = '')
    for j in dt[i]:
        print(j[0],j[1],"шт",end= " ")
    print()
