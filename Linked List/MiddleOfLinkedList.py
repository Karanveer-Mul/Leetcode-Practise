head = [1,2,3,4,5]

node1 = head
node2 = head.next

while (node2 != None):

    node1 = node1.next

    node2 = node2.next
    if (node2 != None):
        node2 = node2.next

print(node1) 