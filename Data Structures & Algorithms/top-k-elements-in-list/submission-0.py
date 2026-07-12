class Solution:
    # return the k most frequest elements in an array
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = nums.count(num)
        print(hashmap)
        top_k = heapq.nlargest(k, hashmap.items(), key=lambda item: item[1])
        li = [num for num, count in top_k]
        return li
        
