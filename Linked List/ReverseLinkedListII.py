# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        i = 1
        dummy = ListNode(0, head)
        prevNode = dummy

        while i < left:
            prevNode = prevNode.next
            i += 1
        
        # Get to the left Node
        curNode = prevNode.next

        for _ in range(right - left):
            nextNode = curNode.next
            curNode.next = nextNode.next
            nextNode.next = prevNode.next
            prevNode.next = nextNode

        return dummy.next