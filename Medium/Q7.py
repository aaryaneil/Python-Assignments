def medianOfList(arr):
    sort_arr = sorted(arr)
    l = len(arr)
    if l%2==1:
        return sort_arr[l//2]
    else:
        mid1 = sort_arr[l//2-1]
        mid2 = sort_arr[l//2]
        return (mid1+mid2)/2
    
print("Median: ", medianOfList([1,2,3,4,5,6,7,8]))