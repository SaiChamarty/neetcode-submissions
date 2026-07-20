class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        print(ans)
        for i in range(0, len(nums)):
            ans.append(nums[i])
        return ans