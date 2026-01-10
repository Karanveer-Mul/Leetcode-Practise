# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root == None:
            return None

        if root.left == None and root.right == None:
            if root.val != key:
                return root
            return None

        if root.val == key:

            nodes = []
            stack = []

            while root or stack:

                if root:
                    stack.append(root) 
                    root = root.left
                else:
                    root = stack.pop()
                    if root.val != key:
                        nodes.append(root.val)
                    root = root.right
            
            n = len(nodes)
            mid = n // 2
            newRoot = TreeNode(nodes[mid])

            queue = deque()
            queue.append((newRoot, 0, mid -1))
            queue.append((newRoot, mid + 1, n - 1))

            while queue:

                parent, left, right = queue.popleft()

                if left <= right:

                    mid = left + (right-left)//2
                    child = TreeNode(nodes[mid])

                    if nodes[mid] < parent.val:
                        parent.left = child
                    else:
                        parent.right = child

                    queue.append((child, left, mid - 1))
                    queue.append((child, mid + 1, right))

            return newRoot

        curr = root
        keyParent = None
        is_left_child = False

        while curr:

            if curr == None:
                return None

            if curr.val == key:
                break
            keyParent = curr
            if curr.val > key:
                curr = curr.left
                is_left_child = True
            else:
                curr = curr.right
                is_left_child = False

        #Now curr should be equivalent to key TreeNode

        keyNode = curr

        nodes = []
        stack = []

        while keyNode or stack:

            if keyNode:
                stack.append(keyNode)
                keyNode = keyNode.left

            else:
                keyNode = stack.pop()
                if keyNode.val != key:
                    nodes.append(keyNode.val)
                keyNode = keyNode.right
        
        if not nodes:
            # No nodes left, just remove the connection
            newChildNode = None
        else:
            n = len(nodes)
            mid = n // 2
            newChildNode = TreeNode(nodes[mid])

            queue = deque()
            queue.append((newChildNode, 0, mid - 1))
            queue.append((newChildNode, mid + 1, n - 1))

            while queue:

                parent, left, right = queue.popleft()

                if left <= right:

                    mid = left + (right - left)//2

                    child = TreeNode(nodes[mid])

                    if nodes[mid] < parent.val:
                        parent.left = child
                    else:
                        parent.right = child

                    queue.append((child, left, mid - 1))
                    queue.append((child, mid + 1, right))

        if keyParent:
            if is_left_child:
                keyParent.left = newChildNode
            else:
                keyParent.right = newChildNode

        return root