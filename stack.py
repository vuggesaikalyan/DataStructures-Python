n = input()
l = []
for i in range(0, 54):
    a = 2 ^ i
    l.append(a)
if n in l:
    print("yes")
else:
    print("no")
