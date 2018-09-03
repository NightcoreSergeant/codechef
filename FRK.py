c = "chef"
c = [c[i]+c[i+1] for i in range(0,3)]
u = 0
for i in range(int(input())):
    X = input()
    for i in c:
        if i in X:
            u+=1
            break
print(u)