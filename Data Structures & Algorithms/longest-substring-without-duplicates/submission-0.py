class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_set = set()
        max_len = 0
        
        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len

