class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i, n in enumerate(nums):
            m = target - n 
            if m in storage:
                return [storage[m], i]
            storage[n] = i
        
        