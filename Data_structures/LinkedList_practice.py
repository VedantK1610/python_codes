'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_at_index(self,data,index):
        if index==0:
            self.insert_at_beg(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1

    def remove_at_index(self,index):
        if index==0:
            self.head=self.head.next
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1

    def reverseLinkedList(self):
        prev = None
        current = self.head

        while current:
            store = current.next
            current.next = prev
            prev = current
            current = store
        self.head = prev
        self.print_linked_list()

l1 = LinkedList()
l1.insert_at_beg(3)
l1.insert_at_beg(2)
l1.insert_at_end(4)
l1.insert_at_index(5,2)
l1.remove_at_index(2)
l1.print_linked_list()
l1.reverseLinkedList()