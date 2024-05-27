# Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    unpacked=[]
    while True:
        unpacked.append(head.val)
        if head.next:
            head=head.next
        else:
            return unpacked[::-1]

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head)) #[5, 4, 3, 2, 1]