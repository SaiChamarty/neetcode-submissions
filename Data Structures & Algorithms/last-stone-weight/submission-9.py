import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        # print(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, -(x - y))
            elif x < y:
                heapq.heappush(stones, -(y - x))
            else:
                continue
        if not stones:
            return 0
        else:
            return -(stones[0])