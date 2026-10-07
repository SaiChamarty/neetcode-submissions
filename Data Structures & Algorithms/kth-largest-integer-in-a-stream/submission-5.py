import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # create a heap of k elements - maybe the first three elements of nums
        self.top_k_heap = nums[:k]
        heapq.heapify(self.top_k_heap) # heapify the top k elements
        for num in nums[self.k:]:
            if num > self.top_k_heap[0]:
                heapq.heappushpop(self.top_k_heap, num) # add a new big element

    def add(self, val: int) -> int:
        # now that we have a heap of first k elements, lets add the new element and loop through the rest of them
        if len(self.top_k_heap) < self.k:
            heapq.heappush(self.top_k_heap, val)
        elif val > self.top_k_heap[0]:
            heapq.heappushpop(self.top_k_heap, val)
        return self.top_k_heap[0]

