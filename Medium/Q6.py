def powerOf2(num):
    num = num/2
    if num==2:
        return True
    elif num>2:
        return powerOf2(num)
    else:
        return False
    
num= int(input("Enter the number: "))
print(powerOf2(num))