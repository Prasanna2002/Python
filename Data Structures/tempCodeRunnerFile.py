class Node(object):
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None

class CLL(object):
    def __init__(self):
        self.head=Node() 
        self.tail=self.head 
        self.disp=0 
    
    def append(self,i):
        if self.head.data==None: 
            self.head.data=i 
            self.disp+=1

        else: 
            self.tail.next=Node(i)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next 

            self.tail.next =self.head 
            self.head.prev=self.tail 
            self.disp+=1
            
    def insert_first(self,i): 
        a=Node(i)
        a.next=self.head 
        a.prev=self.tail 
        self.tail.next=a 
        self.head=a 
        self.disp+=1 

    def insert_last(self,i):
        d=Node(i) 
        d.next=self.head 
        d.prev=self.tail 
        self.tail.next=self.head.prev=d  
        self.tail = d 
        self.disp+=1

    def delete_first(self): 
        self.head.data=self.head.next.data 
        self.head.next =self.head.next.next 
        self.disp-=1

    def delete_last(self): 
        self.tail.prev.next=self.tail.next 
        self.tail=self.tail.prev
        self.disp-=1

    def display(self):
        s=self.head.next
        v=[self.head.data] 
        while s.data!=self.tail.next.data: 
            v.append(s.data) 
            s=s.next 
        print(v) 

    def merge(self,other): 
        self.tail.next=other.head
        self.tail.next.prev=self.tail 

        self.tail=other.tail
        self.tail.next=self.head
        self.disp+=other.disp 

    def reverse(self):
        x,c,y=self.head,0,self.tail
        if self.disp%2==0:pass 
        else:self.disp+=1
        while c<self.disp/2: 
            x.data,y.data=y.data,x.data
            x=x.next 
            y=y.prev
            c+=1

    def count(self):
        print(self.disp)

    def removeduplicate(self): 
        s=self.head 
        while s.next.data!=self.head.data: 
            r=s.next 
            while r.data!=self.head.data: 
                if r.data==s.data: 
                   r.prev.next=r.next 
                r=r.next 
            s=s.next          
s=CLL() 
s.append(90)
s.append(91)
s.append(8989)
s.append(9999)
s.append(8)
s.append(8)
s.append(9999)
s.append(90)
s.removeduplicate()
s.display()
