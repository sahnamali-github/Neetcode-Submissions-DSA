class Solution:
    def trap(self, height: List[int]) -> int:
        # premax = [0]*len(height)
        # premax[0] = height[0]
        # for i in range(1,len(height)):
        #     premax[i] =(max(premax[i-1],height[i]))
        # postmax=[0]*len(height)
        # postmax[len(height)-1] = height[len(height)-1]
        # for i in range(len(height)-2,-1,-1):
        #     postmax[i] = (max(height[i],postmax[i+1]))
        # res = 0
        # for i in range(len(height)):
        #     res += min(premax[i], postmax[i]) - height[i]
        # return res

        # premax = [0]*len(height)
        # for i in range(1,len(height)):
        #     premax[i] =(max(premax[i-1],height[i-1]))
        # postmax=[0]*len(height)

        # for i in range(len(height)-2,-1,-1):
        #     postmax[i] = (max(height[i+1],postmax[i+1]))
        # res = 0
        # for i in range(len(height)):
        #     if height[i] > min(premax[i], postmax[i]):
        #         continue
        #     else:
        #         res += min(premax[i], postmax[i]) - height[i]
        # return res

        # res = 0
        # n = len(height)
        # maxL, maxR = height[0], height[n-1]
        # curr = height[0]
        # l,r = 0, n-1
        # while l < r:
        #     res += (min(maxL,maxR)-curr) if curr < min(maxL,maxR) else 0
        #     maxL = height[l] if height[l] > maxL else maxL
        #     maxR = height[r] if height[r] > maxR else maxR
        #     if height[l] >= height[r]:
        #         r -= 1
        #         curr = height[r]
        #     else:
        #         l += 1
        #         curr = height[l]
        # return res



        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR- height[r]
        return res





        

       