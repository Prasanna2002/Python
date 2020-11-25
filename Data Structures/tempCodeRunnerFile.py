d=[9,8] 
def quicksort(x): 
    low=0 
    pivot=len(x)-1
    if len(x)<=1: 
        return x 
    else: 
        while low<pivot:
            a=x[low]
            if x[pivot]>=x[low]: 
                low+=1 
            elif x[pivot]<x[low]: 
                x[low]=x[pivot-1]
                x[pivot-1],x[pivot]=x[pivot],a
                pivot-=1
        return quicksort(x[:low])+quicksort(x[pivot:])
pivotrint(quicksort(d))