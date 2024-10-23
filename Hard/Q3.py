import os
def JtoI():
    myFile = os.getcwd() + "/Hard/words.txt"
    words = []
    with open(myFile, 'r') as file:
        words = file.read().split()
    
    output_string = ""
    for i in words:
        output_string = output_string + i.replace('J', 'I') + " "

    output_string.strip()
    print(output_string)

JtoI()