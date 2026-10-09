class node:
    def __init__(self,values):
        self.data=values
        self.next=None

class revision:
    def __init__(self):
        self.head=None
    def append (self , new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def print_list(self):
            temp=self.head
            while(temp):
                print(temp.data,end="->")
                temp=temp.next         

list2=revision()
n1=node(80)
n2=node(40)
list2.append(n1)
list2.append(n2)
list2.append(node(30))
list2.append(node(90))
list2.print_list()



            
            


