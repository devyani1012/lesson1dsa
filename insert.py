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

            while temp.next:
                temp=temp.next
            temp.next=new_node

    def insert(self,new_node,pos):
        if pos==1:
           new_node.next= self.head
           self.head=new_node
        else :
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node    
                 

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next    
list1=sll()
n1=node(10)
n2=node(20)
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
list1.print()  

list1.insert(node(54),1)
print("After inserting at position 1")
list1.print()


list1.insert(node(44),4)
print("After inserting at position 4")
list1.print()




        
