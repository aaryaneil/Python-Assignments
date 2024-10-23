def calc_perfect_number():
    num= int(input("Enter a number: "))
    sum=0
    for i in range(1, int(num/2)+ 1):
        if num%i==0:
            sum+=i
    if num==sum:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")

calc_perfect_number()