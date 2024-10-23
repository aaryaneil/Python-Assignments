def digitSum(n):

    if n<10:
        return n
    
    x = n
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    
    return(digitSum(sum))


n = int(input("Enter a number: "))

print(digitSum(n))