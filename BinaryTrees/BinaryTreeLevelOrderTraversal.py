# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []

        Output = {}

        if root == None:
            return output

        def helper(node, level):
            if node == None:
                return

            if level not in Output:
                Output[level] = [node.val]
            else:
                Output[level].append(node.val)
            
            if node.left != None:
                helper(node.left, level+1)
            if node.right != None:
                helper(node.right, level+1)
        
        helper(root, 1)

        for level in sorted(Output.keys()):
            output.append(Output[level])

        return output