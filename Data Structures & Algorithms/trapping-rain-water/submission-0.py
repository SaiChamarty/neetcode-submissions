class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = [0]*len(height)
        curr_max_left = 0
        curr_max_right = 0
        total = 0
        for i,h in enumerate(height):
            if height[i-1] > curr_max_left and i != 0:
                curr_max_left = height[i-1]
            max_left.append(curr_max_left)
        print(max_left)
        
        for j in range(len(height)-1, -1, -1):
            if j != len(height)-1 and height[j+1] > curr_max_right :
                curr_max_right = height[j+1]
            max_right[j] = curr_max_right
        print(max_right)

        for i, num in enumerate(height):
            curr = min(max_left[i], max_right[i]) - num
            if curr < 0:
                continue
            total = total + curr
        return total

