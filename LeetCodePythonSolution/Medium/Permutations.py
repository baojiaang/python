# Given a collection of distinct integers, return all possible permutations.
# 回溯法+dfs
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, hash_set, path, res):
            if depth == size:
                res.append(path[:]) # path 所有元素
                return
            for i in range(size):
                if not nums[i] in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, hash_set, path, res)
                    # 当前数字dfs结束
                    path.pop()
                    hash_set.remove(nums[i])

        size = len(nums)
        if size == 0:
            return []
        res = []
        path = []
        hash_set = set()
        dfs(nums, size, 0, hash_set, path, res)
        return res



