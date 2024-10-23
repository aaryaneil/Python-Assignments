def calc_freq(items):

    freq = {}
    for i in items:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    print("Frequency count: ",freq)

calc_freq([1,2,3,1,2,2,2,2,3,3,])