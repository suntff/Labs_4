s = str(input()).split()
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s.count(s[j]) > s.count(s[i]):
            s[i], s[j] = s[j], s[i]
        elif s.count(s[j]) == s.count(s[i]) and sorted([s[i],s[j]])!=[s[i],s[j]]:
            s[i],s[j]=s[j],s[i]
st = set()
for i in range(len(s)):
    m = len(st)
    st.add(s[i])
    if m<len(st):
        print(s[i])

