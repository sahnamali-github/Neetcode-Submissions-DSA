class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = (l + r)//2
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid 
        # return nums[l]


        # res = nums[0]
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res,nums[l])
        #         break
        #     m = (l + r)//2
        #     res = min(res, nums[m])
        #     if nums[l] <= nums[m]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res

        mnm = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r)// 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                mnm = min(mnm, nums[m])
                r = m - 1
        return mnm       

        # METHOD 1
        # l, r = 0, len(nums) - 1
        # if len(nums) == 1:
        #         return nums[0]
        # while l <= r:
        #     if nums[l] > nums[r] and nums[r] > nums[r - 1]:
        #         r -= 1
        #     elif nums[l] > nums[r] and nums[r] < nums[r - 1]:
        #         return nums[r]
        #     elif nums[l] < nums[r]:
        #         return nums[l]
        #     else:
        #         l += 1
        # return -1

        # METHOD 2
        # mnm = nums[0]
        # for n in nums:
        #     if n < mnm:
        #         mnm = n
        # return mnm

        

        