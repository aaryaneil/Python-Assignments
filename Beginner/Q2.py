def count_alpha_digits():
    x = input("Enter your string: ")
    alpha=0
    num=0
    for i in x:
        if i.isalpha():
            alpha+=1
        elif i.isnumeric():
            num+=1
    print('Alphabets: %d String: %d' % (alpha, num))

count_alpha_digits()    