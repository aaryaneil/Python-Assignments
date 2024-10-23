def uniqueElements(a):
    a_dict = {}
    for i in a:
        if i not in a_dict:
            a_dict[i]=1

    return list(a_dict.keys())

a = [1,2,2,3,4,5,5,6,6,7,7,7,8]

print(uniqueElements(a))