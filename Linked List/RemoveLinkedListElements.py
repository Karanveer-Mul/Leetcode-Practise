class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        curNode = head

        while curNode != None:   
            nextNode = curNode.next            
            while nextNode != None and int(nextNode.val) == val:
                nextNode = nextNode.next

            curNode.next = nextNode
            curNode = curNode.next        

    

        return head

Solution().removeElements([7,7,7,7], 7)