def cafe(num, str):
    using = set()
    left = 0
    user_count = 0


    for i in str:
        if i not in using:
            if user_count < num:
                using.add(i)
                user_count+=1
            else:
                left+=1
        else:
            if i in using:
                using.remove(i)
                user_count-=1
    print(using)
    return left



print(cafe(3,"GACCBDDBAGEE"))