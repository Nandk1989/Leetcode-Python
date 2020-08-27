"""
    Given two binary trees original and cloned and given a reference to a node 
    target in the original tree.
    The cloned tree is a copy of the original tree.
    Return a reference to the same node in the cloned tree.
    Note that you are not allowed to change any of the two trees or the target 
    node and the answer must be a reference to a node in the cloned tree.
    Follow up: Solve the problem if repeated values on the tree are allowed.

    Example 1:
        original      cloned
           7              7
          / \ vTARGET    / \
         4   3          4   3
            / \            / \
           6  19          6  19 

    Input: tree = [7,4,3,null,null,6,19], target = 3
    Output: 3
    Explanation: In all examples the original and cloned trees are shown. 
                 The target node is a green node from the original tree. 
                 The answer is the yellow node from the cloned tree.

    Constraints:
        - The number of nodes in the tree is in the range [1, 10^4].
        - The values of the nodes of the tree are unique.
        - target node is a node from the original tree and is not null.
"""
#Difficulty: Medium
#56 / 56 test cases passed.
#Runtime: 640 ms
#Memory Usage: 23.5 MB

#Runtime: 640 ms, faster than 98.98% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
#Memory Usage: 23.5 MB, less than 42.18% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        while True:
            if cloned:
                stack.append(cloned)
                cloned = cloned.left
            elif stack:
                cloned = stack.pop()
                if cloned.val == target.val:
                    return cloned
                cloned = cloned.right
