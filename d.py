nums=list(map(int,input().split()))
sum2=[]
k=int(input())
for i in nums:
    for j in nums:
        if(i!=j):
            summ=i+j
            sum2.append(summ)

if k in sum2:
    print("True")
