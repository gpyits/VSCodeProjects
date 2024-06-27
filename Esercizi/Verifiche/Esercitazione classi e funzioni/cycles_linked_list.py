# Given head, the head of a linked list, determine if the linked list has a cycle in it. 
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter. 
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Model the Node and Linked List concepts using classes.
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def append(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
        else:
            new_head=Node(val)
            new_head.next=self.head
            self.head=new_head
    def get_node(self, val: int) -> Node:
        while True:
            if self.head.next and self.head.val!=val:
                self.head=self.head.next
            else:
                return self.head
        
def has_cycle(head: Node) -> list[int]:
    seen_nodes=[]
    while head.next:
        seen_nodes.append(head)
        if head.next not in seen_nodes:
            head=head.next
        else:
            return True
    return False


ll2 = LinkedList()
for i in range(5):
    ll2.append(i)
print(has_cycle(ll2.head)) #False 	

ll4 = LinkedList()
ll4.append(1)
node = ll4.head
node.next = node
print(has_cycle(ll4.head)) #True