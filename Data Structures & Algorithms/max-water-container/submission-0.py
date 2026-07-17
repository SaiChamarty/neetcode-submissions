class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0

        while left < right:
            current_vol = min(heights[left], heights[right]) * (right - left) # h * b
            max_vol = max(current_vol, max_vol)
            if heights[left] >= heights[right]:
                right -= 1
                continue
            else:
                left += 1
                continue
        return max_vol
        