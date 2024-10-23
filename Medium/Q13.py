def lambdaFunc(string, char):
    x = lambda inp: inp[0] == char
    print(x(string))

string = input("Enter a string: ")
char = input("Enter a character: ")

lambdaFunc(string, char)
