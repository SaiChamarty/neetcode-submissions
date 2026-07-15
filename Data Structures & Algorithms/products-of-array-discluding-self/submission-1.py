class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1] * prefix[i-1])
        print(prefix)

        result = [1] * len(nums)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                suffix = (nums[i+1] * suffix)
            result[i] = suffix * prefix[i]

        return result
            