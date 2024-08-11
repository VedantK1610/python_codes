class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node

    def print_LL(self):
        itr=self.head
        s=''
        while itr:
            s+=str(itr.data) + ' -->'
            itr=itr.next
        print(s)

    def remove_duplicate(self):
        if self.head is None:
            return

        itr=self.head
        seen={}
        prev=None

        while itr:
            if itr.data in seen:
                prev.next=itr.next
            else:
                seen[itr.data]=True
                prev=itr
            itr=itr.next

ll=LinkedList()
ll.insert_at_beg(3)
ll.insert_at_beg(2)
ll.insert_at_beg(3)
ll.print_LL()
ll.remove_duplicate()
ll.print_LL()