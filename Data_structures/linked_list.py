class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    # def remove_at(self,index):
    #     if index<0:
    #         raise Exception("enter valid index")
    #     if index==0:
    #         self.head=self.head.next
    #         return
    #     count=0
    #     itr=self.head
    #     while itr:
    #         if count==index-1:
    #             itr.next=itr.next.next
    #         itr=itr.next
    #         count+=1

    def remove_element(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next



if __name__=='__main__':
    l1=linked_list()
    l1.insert_at_begining(5)
    l1.insert_at_begining(4)
    l1.insert_at_end(6)
    l1.remove_element(5)
    l1.print_linked_list()
