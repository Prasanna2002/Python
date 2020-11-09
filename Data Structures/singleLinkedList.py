class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

class singlelinkedlist(object):
    def __init__(self):
        self.head=Node()
        self.duplicate=self.head

        self.tail=self.head
        self.disp=0
        
    def append(self,i):
        if self.head.data==None: 
            self.head.data=i
            self.disp+=1
        else:
            self.tail.next=Node(i)
            self.tail=self.tail.next
            self.disp+=1

    def insert_first(self,i):
        d,w=Node(i),self.head
        self.head=d
        self.head.next=w

    def insert_last(self,i):
        self.tail.next=Node(i)
        self.tail=self.tail.next  

    def delete_first(self):
        self.head=self.head.next

    def delte_last(self):
        self.tail.data=None

    def search(self,i):
        e=self.head
        try:
            while e.data!=i:
                e=e.next
            print(True)
        except:
            print(False)

    def count(self,i):
        s=self.head
        a=0
        while s!=None:
            if s.data==i:
                a+=1
            s=s.next
        return a

    def merge(self,other):
        self.tail.next=other.head
        self.tail=other.tail
        self.disp+=other.disp
            
    def removeduplicate(self):
        s=self.head
        while s!=None:
            r=s.next
            while r!=None:
                if r.data==s.data:
                    if r.next!=None:
                        r.data=r.next.data 
                        r=r.next
                    else:
                        r.data=None 
                    self.disp-=1
                r=r.next
            s=s.next

    def _return_(self):
        x,y=self.head,[]
        while x!=None:
            if x.data==None:
                pass
            else:
                y.append(x.data)
            x=x.next      
        return list(reversed(y))

    def reverse(self):
        s,r=self._return_(),self.head
        v=0
        while v<=len(s)-1:
            r.data = s[v]
            v+=1 
            r=r.next 

    def display(self):
        x,y=self.head,[]
        while x!=None:
            if x.data==None:
                pass
            else:
                y.append(x.data)
            x=x.next      
        print(y)

    

        



