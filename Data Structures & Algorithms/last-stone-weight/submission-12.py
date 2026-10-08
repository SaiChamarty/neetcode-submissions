import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate in-place to save memory (O(1) auxiliary space)
        for i in range(len(stones)):
            stones[i] = -stones[i]
            
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            # x is always <= y. If they are unequal, a stone remains.
            if x != y:
                # x is the more negative number, so x - y directly yields the negative remainder
                heapq.heappush(stones, x - y)
                
        return -stones[0] if stones else 0