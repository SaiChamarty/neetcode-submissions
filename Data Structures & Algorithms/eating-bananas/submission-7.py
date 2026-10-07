class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # what I plan to do is loop through the new sorted list from smallest to largest and calculate how many hours each is taking and the first one less than h. 
        # for k in range(1, max(piles)+1):
        #     count = 0
        #     for pile in piles:
        #         count += -(-pile // k) # ceiling division
        #     if count <= h: 
        #         return k
        # what we looked for up there is the minimum hours that took to eat up every pile - from range (1 to max(piles) + 1). Instead of looping through the whole range, we can use binary search to make the search more efficient, but same logic. 
        l = 1
        r = max(piles)
        count = 0
        res = 0
        while l <= r:
            mid = (l + r) // 2
            count = sum(-(-pile // mid) for pile in piles)
            if count <= h:
                res = mid
                r = mid - 1
            elif count > h:
                # taking too many hours, so increase the rate...
                # that means make l = mid
                l = mid + 1
        return res
