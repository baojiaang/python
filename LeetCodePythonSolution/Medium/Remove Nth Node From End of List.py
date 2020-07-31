# Given a linked list, remove the n-th node from the end of list and return its head.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
# My Solution: Hashmap
# Other Solution: two pointer, the first pointer move n+1 position, then the second pointer start to move, when first pointer
# meet the end, the second pointer position is the position that need to delete

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            curNode = head
        dict ={}
        index = 0
        while curNode:
            dict.update({index:curNode})
            curNode = curNode.next
            index += 1
        index -= 1
        find_index = index - n + 1
        if find_index is 0:
            if head.next is None:
                return None
            else:
                return head.next
        elif find_index is index:
            preNode = dict[find_index - 1]
            preNode.next = None
        else:
            preNode = dict[find_index-1]
            nextNode = dict[find_index+1]
            preNode.next = nextNode
        return head
