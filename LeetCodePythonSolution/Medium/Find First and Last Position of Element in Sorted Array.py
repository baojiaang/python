from typing import List
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#  二分法 缩小左右区间， 找到左右边界

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound():
            left = 0
            right = size-1
            while left <= right:
                mid = int(left + (right-left)/2)
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                elif nums[mid] == target:
                    right = mid-1  # 缩小右区间

            if left >= size or nums[left] != target:
                return -1

            return left

        def right_bound():
            left = 0
            right = size-1

            while left <= right :
                mid = int(left +(right-left)/2)
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                elif nums[mid] == target:
                    left = mid+1  # 缩小左区间

            if right<0 or nums[right] != target:
                return -1

            return right
        size = len(nums)
        if size == 0:
            return [-1,-1]
        elif size == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        else:
            l = left_bound()
            r = right_bound()
            res = [l,r]
            return res


if __name__=="__main__":
    s = Solution()
    nums = [2,2]
    target = 3
    print(s.searchRange(nums,target))



