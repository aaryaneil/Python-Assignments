import os

def evenStrings():
    myFile = os.getcwd() + "/Hard/doc.txt"
    fileContent = ""
    with open(myFile, 'r') as file:
        fileContent = file.read()
    
    words = fileContent.split()
    evenWords = []
    for i in words:
        if len(i)%2==0:
            evenWords.append(i)
    
    with open(myFile, 'w') as file:
        for i in evenWords:
            file.write(i+"\n")

evenStrings()