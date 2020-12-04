def binary_search(x,low,high,r):
    while low<=high:
        mid=(low+high)//2
        if x[mid]>r: 
            high=high-1 
        elif x[mid]<r: 
            low=mid+1 
        elif x[mid]==r: 
            return mid
    return -1 

