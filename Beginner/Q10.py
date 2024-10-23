def reverseString():
    input_string = input("Enter a string: ")
    words = input_string.split(" ")
    output_string = ""
    for i in reversed(words):
        output_string = output_string+ i +" "
    output_string.strip()
    

    print("Your output is : ",output_string)

reverseString()