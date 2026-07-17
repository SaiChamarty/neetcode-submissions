class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        left = 0
        right = len(nums)-1
        answer = []
        for i, num in enumerate(nums):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            # if current num == previous num, continue because the triplet will repeat
            if i > 0 and num == nums[i-1]:
                continue
            while left < right:
                if nums[left] + nums[right] > target:
                    # number too big, reduce sum - decrement right
                    right = right - 1
                elif nums[left] + nums[right] < target:
                    # number too small, increase sum - increment left
                    left = left + 1
                else:
                    answer.append([num, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    # now if next left is the same as current left, we keep moving left by 1
                    # We will avoid the same triplet that way
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
        return answer
                

                
