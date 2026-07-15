class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(1)
            else:
                result.append(nums[i-1] * result[i-1])
        print(result)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                suffix = (nums[i+1] * suffix)
            result[i] = suffix * result[i]

        return result
            