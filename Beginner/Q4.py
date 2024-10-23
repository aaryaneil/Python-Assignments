def sum_odd_number():
    sum=0
    start = int(input("Enter starting number:"))
    stop = int(input("Enter ending number: "))
    
    for i in range(start, stop+1):
        if i%2==1:
            sum+=i
    
    print("Sum: ", sum)

sum_odd_number()