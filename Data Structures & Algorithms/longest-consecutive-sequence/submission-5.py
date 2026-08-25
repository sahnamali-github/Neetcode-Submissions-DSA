class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count = 0
        # max_count = 0
        # for n in (nums):
        #     if (n - 1) not in nums:
        #         count = 1
        #         while (n+1) in nums:
        #             n += 1
        #             count += 1
        #     max_count = max(count,max_count)
        # return max_count

        # METHOD 1 
        # numSet = set(nums)
        # res = 0
        # count = 0
        # for n in numSet:
        #     curr = n
        #     count = 1
        #     while curr+1 in numSet:
        #         count += 1
        #         curr += 1
        #     res = max(res, count)
        # return res

        # METHOD 2
        numSet = set(nums)
        maxL = 0
        for n in numSet:
            if n - 1 in numSet:
                continue
            count = 1
            curr = n
            while curr + 1 in numSet:
                count += 1
                curr += 1
            maxL = max(count, maxL)
        return maxL


        



        
        
       
        






        