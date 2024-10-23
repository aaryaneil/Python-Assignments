def sumPair(n,k):
    pairCount=0
    for i in range(0,len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]+n[j] == k:
                pairCount+=1
    return pairCount

n = [1,2,3,4,5]
k=6
print(sumPair(n,k))