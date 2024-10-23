def commonElements(a,b):
    return list(set(a).intersection(b))

a = [1,2,3,4]
b = [2,3,4]

print(commonElements(a,b))