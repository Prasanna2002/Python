def bubblesort(x): 
    y=len(x)
    for j in range(y):
        for i in range(0,y-j-1): 
            if x[i]>x[i+1]: 
                x[i],x[i+1]=x[i+1],x[i]
    
    


    




