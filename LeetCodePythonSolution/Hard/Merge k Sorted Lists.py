# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# My Solution: priority queue
# Divide and conquer also works
# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # 自定义 lt 添加 到 leetcode所给的 Listnode
        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__


        head = ListNode(0)
        curNode = head
        pq = []
        for node in lists:
            if node:
                heapq.heappush(pq,node)

        while len(pq) > 0:
            cur = heapq.heappop(pq)
            curNode.next = cur
            curNode = curNode.next
            if cur.next:
                heapq.heappush(pq,cur.next)
        return head.next

if __name__=="__main__":
    s = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    node = s.mergeKLists(lists)
    print(node.val)
