# Definition for a binary tree node.
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# deep copy / shallow copy
# 深浅拷贝
# 在 Python 中，对象赋值实际上是对象的引用。当创建一个对象，然后把它赋给另一个变量的时候，Python 并没有拷贝这个对象，而只是拷贝了这个对象的引用，我们称之为浅拷贝。
#
# 在 Python 中，为了使当进行赋值操作时，两个变量互补影响，可以使用 copy 模块中的 deepcopy 方法，称之为深拷贝。
#
# append() 函数
#
# 当 list 类型的对象进行 append 操作时，实际上追加的是该对象的引用。
#
# id() 函数：返回对象的唯一标识，可以类比成该对象在内存中的地址。
#
# >>>alist = []
# >>> num = [2]
# >>> alist.append( num )
# >>> id( num ) == id( alist[0] )
# True
# 如上例所示，当 num 发生变化时(前提是 id(num) 不发生变化），alist 的内容随之会发生变化。往往会带来意想不到的后果，想避免这种情况，可以采用深拷贝解决：
# alist.append( copy.deepcopy( num ) )
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node,cur_list,target):
            if not node:
                return
            # cur_list.append(node.val)

            if not node.left and not node.right and node.val == target:
                # self.res.append(cur_list.copy())  # 或者这个方法
                self.res.append(cur_list)
                cur_list += [node.val]  # 产生一个深拷贝， 被这个坑了好久
            dfs(node.left,cur_list+[node.val],target-node.val)
            dfs(node.right,cur_list+[node.val],target-node.val)
            # dfs(node.left, cur_list, target - node.val)
            # dfs(node.right, cur_list, target - node.val)
            # cur_list.pop()   # 回溯
        self.res=[]
        cur_list = []
        dfs(root,cur_list,sum)
        return self.res
