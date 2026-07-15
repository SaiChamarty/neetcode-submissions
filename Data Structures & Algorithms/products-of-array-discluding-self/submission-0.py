class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1] * prefix[i-1])
        print(prefix)

        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                suffix[i] = (nums[i+1] * suffix[i+1])
        print(suffix)

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result
            