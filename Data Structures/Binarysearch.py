x=[i for i in range(100,0,-1)] 
d=False 
while d!=True:
    r=0
    for i in range(len(x)-1): 
        if x[i]>x[i+1]: 
            x[i],x[i+1]=x[i+1],x[i]
            r+=1 
    if r==0: 
        print(x) 
        d=True 
    
    


    




