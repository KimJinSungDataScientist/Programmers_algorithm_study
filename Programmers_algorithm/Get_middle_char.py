s = "qwer"

middle = len(s)//2
save = ""

if len(s)%2==0:
    save += s[middle-1:middle+1]
else:
    save = s[middle]

print(save)