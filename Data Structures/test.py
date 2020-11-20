x=list(map(int,input().split())) 
def insertionSort(x):
    for i in range(1,len(x)): 
        k=x[i] 
        j=i-1 
        while j>=0 and x[j]>k: 
            x[j+1]=x[j] 
            j=j-1 
        x[j+1]=k 
insertionSort(x) 
print(x)

