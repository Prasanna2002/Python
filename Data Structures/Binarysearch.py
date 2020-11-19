x=list(map(int,input("Enter the Numbers:").split()))
def binarysearch(x):
    search=int(input("Enter A Number: "))
    low=0 
    mid=0
    high=len(x)-1 
    while mid<=high and mid<len(x)-1: 
        mid=(low+high)//2
        if x[mid]>search: 
            high=high-1 
        elif x[mid]<search: 
            low=mid+1 
        elif x[mid]==search: 
            return x[mid]
    return -1 

print(binarysearch(x))
