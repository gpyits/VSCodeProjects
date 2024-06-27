#Given the head of a singly linked list, return true if it is a palindrome. 
#Model the Node and Linked List concepts using classes.
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    def unpacker(self) -> list[int]:
        unpacked=[]
        while True:
            unpacked.append(self.val)
            if self.next:
                self=self.next
            else:
                return unpacked

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
        
def is_palindrome(head: Node) -> list[int]:
    return head.unpacker()==head.unpacker()[::-1]

ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head))