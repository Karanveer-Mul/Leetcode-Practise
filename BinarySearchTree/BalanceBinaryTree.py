# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        nodes = []
        stack = []

        curr = root

        while curr or stack:

            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                nodes.append(curr.val)
                curr = curr.right                

        n = len(nodes)
        mid = n//2
       
        root = TreeNode(nodes[mid])

        queue = deque()
        queue.append((root, 0, mid - 1))
        queue.append((root, mid + 1, n - 1))

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

        return root


