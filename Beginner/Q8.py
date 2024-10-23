import math
def calc_LCM():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    gcd=math.gcd(a,b)
    return (a*b)//gcd


print("Enter numbers to find lcm")
print(calc_LCM())