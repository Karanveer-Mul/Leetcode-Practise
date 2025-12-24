# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Output = {}
        self.helper(root, 0, Output)

        output = []
        for level in sorted(Output.keys()):
            output.append(sum(Output[level]) / len(Output[level]))

        return output

    def helper(self, node, level, Output):

        if node == None:
            return
        
        if level not in Output:
            Output[level] = []

        Output[level].append(node.val)

        self.helper(node.left, level+1, Output)
        self.helper(node.right, level+1, Output)