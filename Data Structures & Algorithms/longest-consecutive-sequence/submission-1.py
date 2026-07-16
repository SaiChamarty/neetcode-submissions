class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in hashset:
            length = 0
            if (num - 1) not in hashset:
                # start of a sequence
                while (num + length) in hashset:
                    length = length + 1
            longest = max(longest, length)
        return longest

            