import os
def countLines():
    myFile = os.getcwd() + "/Hard/demo.txt"
    count = 0
    with open(myFile, 'r') as file:
        count = len(file.readlines())

    print(f"The file has {count} line")

countLines()