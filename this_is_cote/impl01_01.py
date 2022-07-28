h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+"시"+str(j)+"분"+str(k)+"초":
                count += 1

print(count)