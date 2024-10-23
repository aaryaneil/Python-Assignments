def calc_factorial():
    num = int(input("Enter number: "))
    prod=1
    for i in range(1,num+1):
        prod=prod*i
    print("Factorial: ", prod)

calc_factorial()