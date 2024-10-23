def errorHandling(arr):
    print(arr)
    x = int(input("Enter the index you want to access :"))
    try:
        print(arr[x])
    except IndexError:
        print("The index is out of bounds.")


arr = [1, 2, 3, 4, 5]

errorHandling(arr)