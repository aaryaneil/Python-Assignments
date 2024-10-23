def countVowels(str):
    vow_count=0
    for i in str:
        i=i.lower()
        if i == 'a' or i == 'e' or i=='i' or i== 'o' or i=='u':
            vow_count+=1
    return vow_count

str = input("Enter a string: ")

print("Vowels: ", countVowels(str))