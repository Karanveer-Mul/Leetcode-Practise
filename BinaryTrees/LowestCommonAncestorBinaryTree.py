# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ancestor = {}
        node_map = {}

        def buildAncestory(node, ancestorList):

            if node == None:
                return

            if node.val == p.val:
                ancestor[node.val] = ancestorList
            elif node.val == q.val:
                ancestor[node.val] = ancestorList

            if node.val not in node_map:
                node_map[node.val] = node

            if len(ancestor) == 2:
                return

            extended_ancestorList = ancestorList.copy()
            extended_ancestorList.append(node.val)

            if node.left:
                buildAncestory(node.left , extended_ancestorList)
            if node.right:
                buildAncestory(node.right , extended_ancestorList)

        buildAncestory(root, [])

        p_ancestor = ancestor[p.val]     
        q_ancestor = ancestor[q.val]

        # Check if p is an ancestor of q 
        if p.val in q_ancestor:
            return node_map[p.val]
        
        # Check if q is an ancestor of p 
        if q.val in p_ancestor:
            return node_map[q.val]

        LCA = root.val

        m = 0

        while m < len(p_ancestor) and m < len(q_ancestor):
            if p_ancestor[m] == q_ancestor[m]:
                LCA = p_ancestor[m]
                m += 1

            else:
                break
        
        return node_map[LCA]