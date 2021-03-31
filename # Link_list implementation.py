# Link_list implementation
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Link_list:
    def __init__(self):
        self.head=None
    def print_link_list(self):      # To print linklist
        str1=""
        temp=self.head
        while(temp):
            str1=str1+str(temp.data)
            if temp.next:
                str1=str1+'-->'
            temp=temp.next
        return str1
    def get_length(self):     # To find length of linklist
        temp=self.head
        count=0
        while(temp):
            count=count+1
            temp=temp.next
        return count
    def insert_element_at_begining(self,data):
        begining_node=Node(data)
        begining_node.next=self.head
        self.head=begining_node
    def insert_element_at_end(self,data):
        if self.head == None:
            self.head=Node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(data)
        """while(temp):             # why this is not working
            temp=temp.next
        temp=Node(data)"""
    def insert_at_this_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.insert_element_at_begining(data)
            return

        temp=self.head
        count=0
        while(temp):
            if count==index-1:
                new_node=Node(data)
                new_node.next=temp.next.next
                temp.next=new_node
                break
            temp=temp.next
            count=count+1
    def remove_from_this_index(self,index):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
        count=0
        temp=self.head
        while(temp):
            if count==index-1:
                temp.next=temp.next.next
                break
            temp=temp.next
            count=count+1
    def insert_dataset(self,dataset):
        self.head=None
        for data1 in dataset:
            self.insert_element_at_end(data1)










if __name__=='__main__':
    ll=Link_list()
    ll.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    ll.head.next=second
    second.next=third
    third.next=fourth
    #print(ll.print_link_list())
    #print(ll.get_length())
    ll.insert_element_at_begining(5)
    ll.insert_element_at_begining(6)
    #print(ll.print_link_list())
    ll.insert_element_at_end(7)
    ll.insert_element_at_end(8)
    #print(ll.print_link_list())
    ll.insert_at_this_index(2,9)
    #print(ll.print_link_list())
    ll.remove_from_this_index(3)
    #print(ll.print_link_list())
    ll_1 = Link_list()
    ll_1.insert_dataset(["banana","mango","grapes","orange"])
    print(ll_1.print_link_list())
