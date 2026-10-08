import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        # print(max_heap)
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x > y:
                heapq.heappush(max_heap, -(x - y))
            elif x < y:
                heapq.heappush(max_heap, -(y - x))
            else:
                continue
        if not max_heap:
            return 0
        else:
            return -(max_heap[0])