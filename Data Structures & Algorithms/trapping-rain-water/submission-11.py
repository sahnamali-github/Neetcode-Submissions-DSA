class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        Lmax, Rmax = height[l], height[r]
        res = 0
        while l < r:
            if Lmax < Rmax:
                l += 1
                res += max((Lmax - height[l]), 0)
                Lmax = max(Lmax, height[l])
            else:
                r -= 1
                res += max((Rmax - height[r]), 0)
                Rmax = max(Rmax, height[r])
        return res

        