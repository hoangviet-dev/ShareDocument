#n = int(input())

a = [1,3,2,5]

#for i in (1,n):
#    k = int(input())
#    a.append(k)

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i] < a[j]):
            a[i], a[j] = a[j], a[i]

print(a)
print('Max:', max(a))
print('Min:', min(a))
print('Median:', (max(a) - min(a))/len(a))
