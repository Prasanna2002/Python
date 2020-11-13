class Node(object):
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None  

class stack(object):
    def __init__(self): 
        self.head=Node() 
        self.tail=self.head 
        self._top=self.head 
        self.disp=0 

    def push(self,i):
        if self.head.data==None:
            self.head.data=i 

        else:
            self.tail.next=Node(i)
            self.tail.next.prev=self.tail 
            self.tail=self.tail.next  

            self._top=self._top.next 
            self.disp+=1 

    def pop(self): 
        if self.head.data==None:
            print("Stack Underflow")
        else:
            self.tail=self.tail.prev 
            self.tail.next=None 
            self._top=self._top.prev 

    def top(self):
        print(self._top.data)
         

    def display(self): 
        e=self.head;r=[]
        while e!=None:
            if e.data==None: 
                pass 
            else: 
                r.append(e.data)
            e=e.next 
        print(r) 
    
 


e=stack()
e.display()
