class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # res = 0
        # for i in range(len(heights)):
        #     height = heights[i]
        #     left = i
        #     while left >=0 and heights[left] >= height:
        #         left -= 1
        #     right = i
        #     while right < len(heights) and heights[right] >= height:
        #         right += 1
        #     res = max((right-left-1) * height, res )
        # return res

        #Optimal
        maxArea = 0
        stack = []   #(index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h)) 
        while stack:
            index,height = stack.pop()
            maxArea = max(maxArea, height*(len(heights)-index))
        return maxArea
            


