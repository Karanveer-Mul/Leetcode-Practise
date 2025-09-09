head = [1,2,3,4,5]

curNode = head
prevNode = None

while curNode != None and curNode.next != None:
    tmp = curNode
    tmp.next = prevNode
    curNode = curNode.next
    prevNode = tmp

print(prevNode) 