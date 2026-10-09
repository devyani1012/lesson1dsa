class node:
    def __init__(self,value): #constructor
        self.data=value
        self.next=None #two parameters
class sll:     #creating  singly linear linked list
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node   #check head is empty
        else:
            temp=self.head    #if not then this will executed

            while(temp.next):
                temp=temp.next
            temp.next=new_node  
                 

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data ,end="->")
            temp=temp.next    
list1=sll()
n1=node(10)
n2=node(20)
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
list1.print()  



        
