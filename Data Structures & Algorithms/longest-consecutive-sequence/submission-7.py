class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        for n in nums:
            if n - 1 in hashSet:
                continue
            count = 1
            while n + 1 in hashSet:
                count += 1
                n += 1
            maxCount = max(count, maxCount)
        return maxCount
        