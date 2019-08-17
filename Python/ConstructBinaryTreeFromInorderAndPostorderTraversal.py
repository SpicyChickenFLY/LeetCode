# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    
    # RunTime: 71.07%, MemoryUsage: 34.21%
    def buildTree(self, postorder, inorder) -> TreeNode:
        # print(postorder, inorder)
        root = None
        if len(postorder) > 0:
            peak = postorder[-1]
            root = TreeNode(peak)
            postorder.remove(peak)
            partition = inorder.index(peak)
            if partition > 0:
                left_inorder = inorder[:partition]
                root.left = self.buildTree(postorder[:len(left_inorder)], left_inorder)
            if partition < len(inorder) - 1:
                right_inorder = inorder[partition + 1:]
                root.right = self.buildTree(postorder[:-1], right_inorder)
        return root
        

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        (
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3]
        ),
    ]
    for test_case in test_cases:
        print(s.buildTree(test_case[0], test_case[1]))
