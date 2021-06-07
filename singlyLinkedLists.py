class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node=SLNode(val)
        new_node.next=self.head
        self.head=new_node
        return self
    def print_values(self):
        runner=self.head
        while runner!=None:
            print(runner.value)
            runner=runner.next
        return self
    def add_to_back(self, val):
        new_node=SLNode(val)
        runner=self.head
        while runner.next!=None:
            runner=runner.next
        runner.next=new_node
        return self
    def remove_from_front(self):
        self.head=self.head.next
        return self
    def remove_from_back(self):
        last_node=self.head
        while last_node.next.next!=None:
            last_node=last_node.next
        last_node.next=None
        return self
    def remove_val(self, val):
        if self.head.value==val:
            self.remove_from_front()
        else:
            runner=self.head
            while runner.next.value!=val and runner.next.next!=None:
                runner=runner.next
            if runner.next.value==val:
                runner.next=runner.next.next
        return self
    def insert_at(self,val,n):
        if n==0:
            self.add_to_front(val)
        elif n>0:
            insert_node=self.head
            index=0
            while n!=index+1 and insert_node.next!=None:
                insert_node=insert_node.next
                index+=1
            next_node=insert_node.next
            insert_node.next=SLNode(val)
            insert_node.next.next=next_node
        return self

my_list = SList()
my_list.add_to_front("Jim")
my_list.add_to_front("Dwight")
my_list.add_to_front("Andy")

my_list2 = SList()
my_list2.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back('extra').add_to_back('stuff').remove_val('abcd').insert_at('abcd', 5).print_values()