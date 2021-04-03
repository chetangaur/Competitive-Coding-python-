class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubly_linklist():
    def __init__(self):
        self.head=None

    def print_forward(self):
        temp=self.head
        str1=""
        while(temp):
            str1=str1+str(temp.data)+"-->"
            temp=temp.next
        return str1
    def print_backward(self):
        temp=self.head
        str1=""
        while(temp.next):
            temp=temp.next
        last_node=temp
        while(last_node):
            str1=str1+str(last_node.data)+"-->"
            last_node=last_node.prev
        return str1













if __name__=='__main__':

    dll=doubly_linklist()
    dll.head=Node(1)
    first=Node(1)
    second=Node(2)
    third=Node(3)
    dll.head.next=second
    second.next=third
    third.prev=second
    second.prev=first
    print(dll.print_forward())
    print(dll.print_backward())
