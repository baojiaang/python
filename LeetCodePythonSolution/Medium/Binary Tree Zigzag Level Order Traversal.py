# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 层级遍历， 利用flag来控制顺序



from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        import queue
        q = queue.Queue()
        flag = 0
        res = []
        if root:
            q.put(root)
        while q.qsize() > 0:
            cur_list = []
            size = q.qsize()
            for i in range(size):
                node = q.get()
                cur_list.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if flag%2 is 1:
                cur_list.reverse()
            if len(cur_list) > 0:
                res.append(cur_list)
            flag += 1
        return res
