class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplets = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 res.add(triplets)
        # return [list(r) for r in res]


        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] > 0 :
        #         break
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     l, r = i + 1, len(nums)-1
        #     while l < r:
        #         if nums[l] + nums[r] > -nums[i]:
        #             r-= 1
        #         elif nums[l] + nums[r] < -nums[i]:
        #             l += 1
        #         else:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l += 1
        #             r -= 1
        #             while l < r and nums[l] == nums[l -1]:
        #                 l += 1
        # return res


        res = []
        nums.sort()
        for i , a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res





        