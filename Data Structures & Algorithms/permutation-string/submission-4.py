class Solution:
    def permutationMatch(self, s1: str, sub: str) -> bool:
        # are s1 and sub matching (permutation)
        sub = list(sub)
        s1 = list(s1)
        if sorted(s1) == sorted(sub):
            return True
        else:
            return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the length of the window is the length of s1. 
        left = 0
        right = len(s1)
        while right < len(s2)+1:
            result = self.permutationMatch(s1, s2[left:right])
            if result:
                return True
            else: 
                right = right + 1
                left = left + 1
        return False
