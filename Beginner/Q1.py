def num_3_or_5():
    num = int(input("Enter a number"))
    if num%3==0 and num%5==0:
        print("Consultadd - Python Training")
    elif num%3==0:
        print("Consultadd")
    elif num%5==0:
        print("Pyton Training")

num_3_or_5()