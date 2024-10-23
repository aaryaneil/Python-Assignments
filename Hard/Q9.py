def encoded_string(string):
    count = 0
    result=""
    curr_char = string[0]
    for i in string:
        if i == curr_char:
            count+=1
        elif i!=curr_char:
            result = result + curr_char + str(count)
            count = 1
            curr_char = i
    result = result + curr_char + str(count)
    print(result)


encoded_string("wwwweeetttyurrrrr")