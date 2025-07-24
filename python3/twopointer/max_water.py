class Solution:
    def max_area(self, heights):
        left, right, max_water = 0, len(heights) - 1, 0

        while left < right:
            currentMax = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, currentMax)

            if heights[left] >= heights[right]:
                right -= 1
            else: 
                left += 1
        
        return max_water
