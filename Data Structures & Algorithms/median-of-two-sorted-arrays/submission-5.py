class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        val = 0
        for n in nums1:
            res.append(n)
        for n in nums2:
            res.append(n)
        res.sort()
        if len(res) % 2 == 0:
            val = (res[len(res)//2] + res[(len(res)//2) - 1])/2
        else:
            val = res[len(res)//2]
        return val
                

