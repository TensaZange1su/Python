n = 6
mas= [ 5,7,4,3,8,2]
count = 0
for runs in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            mas[i],mas[i+1] = mas[i+1],mas[i]
            count += 1
    print(mas)
print(count)
print(runs)