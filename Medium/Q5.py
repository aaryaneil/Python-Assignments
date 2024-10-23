def weatherData(arr):
    averageTemp = sum(arr)/len(arr)
    minTemp = min(arr)
    maxTemp = max(arr)

    print("Average temperature: ", averageTemp)
    print("Minimum temperature: ", minTemp)
    print("Maximum temperature: ",maxTemp)

arr=[22,23,25,26,27,27,27]

weatherData(arr)