class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            current = (left + right) // 2
            if nums[current] > target:
                right = current
                continue
            elif nums[current] < target:
                left = current + 1
                continue
            elif nums[current] == target:
                return current
        return -1