class Node(object):
    def __init__(self,data=None): 
        self.data=data
        self.prev=None 
        self.next=None 
         
class Queue(object): 
    def __init__(self): 
        self.head=Node() 
        self.tail=self.head
        self.disp=0
    def enqueue(self,i): 
        if self.head.data==None: 
            self.head.data=i 
            self.disp+=1
        else:
            self.tail.next=Node(i)
            self.tail.next.prev=self.head 
            self.tail=self.tail.next 
            self.disp+=1

    def dequeue(self): 
        if self.head.next==None:
            self.head=None
            self.disp-=1
        
        else:
            self.head=self.head.next 
            self.head.prev=None 
            self.disp-=1

    def display(self): 
        while self.head!=None: 
            print(self.head.data,end='--->')
            self.head=self.head.next 

    def length(self):
        print(self.disp)

d=Queue() 
d.enqueue(10)
d.enqueue(100)
d.dequeue()
d.display()