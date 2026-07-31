class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            m = target - n
            if m not in hashMap:
                hashMap[n] = i
            else:
                return [hashMap[m], i]
        
        