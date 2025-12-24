head = [1,2,3,4,5]

curNode = head
prevNode = None

while curNode != None and curNode.next != None:
    nextNode = curNode.next
    curNode.next = prevNode
    prevNode = curNode
    curNode = nextNode

print(prevNode) 