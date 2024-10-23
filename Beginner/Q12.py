def reverseNumber(n):

    sum = 0

    while n>0:
        sum+= n%10
        print(sum)
        sum*=10
        n=n//10

    return(sum//10)

n = int(input("Enter a number: "))

print(reverseNumber(n))