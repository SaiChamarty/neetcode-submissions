class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxL = height[0]
        maxR = height[len(height) - 1]
        total = 0

        while left < right:
            if height[left] <= height[right]:
                curr = min(maxL, maxR) - height[left] # if we moved left. 
                if curr > 0:
                    total += curr
                left += 1
                maxL = max(height[left], maxL)
            else:
                curr = min(maxL, maxR) - height[right] # if we moved right. 
                if curr > 0:
                    total += curr
                right -= 1
                maxR = max(height[right], maxR)
        return total