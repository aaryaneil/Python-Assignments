def anagram():
    a = input("Enter a string: ")
    b = input("Enter anagram string: ")
    a_dict = {}
    b_dict = {}

    for i in a:
        if i in a_dict:
            a_dict[i]+=1
        else:
            a_dict[i]=1
    for i in b:
        if i in b_dict:
            b_dict[i]+=1
        else:
            b_dict[i]=1
    if a_dict == b_dict:
       print("The strings are anagrams.")
    else:
        print("Strings are not anagrams.")

anagram()