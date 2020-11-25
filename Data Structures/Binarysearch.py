def binary_search(x,low,high,r):
    mid=0
    while mid<=high and mid<len(x)-1: 
        mid=(low+high)//2
        if x[mid]>r: 
            high=high-1 
        elif x[mid]<r: 
            low=mid+1 
        elif x[mid]==r: 
            return mid
    return -1 

