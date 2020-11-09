class Node(object):
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None
    
class doublelinkedlist(object):

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
            self.disp+=1

    def insert_first(self,i):
        s=self.head 
        self.head=Node(i)
        self.head.next=s.next.prev
        s.prev=self.head
        self.disp+=1

    def insert_last(self,i):
        self.tail.next=Node(i)
        self.tail.next.prev=self.tail
        self.tail=self.tail.next
        self.disp+=1

    def delete_first(self):
        self.head.data=self.head.next.data
        self.head.next=self.head.next.next
        self.disp-=1

    def delete_last(self):
        self.tail.data=None
        self.tail=self.tail.prev
        self.tail.next=None
        self.display-=1

    def removeduplicate(self):
        s=self.head
        while s!=None:
            r=s.next
            while r!=None:
                if r.data==s.data:
                    if r.next!=None:
                       r.prev.next=r.next
                       r.next.prev=r.prev
                    else:
                        r.prev.next=None
                        self.tail=r.prev
                    r.data=None
                    self.disp-=1
                r=r.next
            s=s.next

    def count(self):
        print(self.disp)
        
    def reverse(self):
        w,x,y=0,self.head,self.tail
        if self.disp%2==0:
            pass
        else:
            self.disp+=1
        while w<(self.disp/2):
            x.data,y.data=y.data,x.data
            x=x.next
            y=y.prev
            w+=1

    def merge(self,other):
        self.tail.next=other.head
        self.tail.next.prev=self.tail
        self.tail=other.tail
        self.disp+=other.disp

    def display(self):
        x,s=self.head,[]
        while x!=None:
            if x.data==None:
                pass
            else:
                s.append(x.data)
            x=x.next 
        print(s) 
