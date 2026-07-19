class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hmap = {}
        
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            if (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

