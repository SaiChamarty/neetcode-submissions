class Solution:
    # return the k most frequest elements in an array
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create n+1 buckets for each frequency from 0 to n
        buckets = [[] for _ in range(len(nums)+1)]
        # count number of items
        hashmap = {}
        result = []
        for i, num in enumerate(nums):
            if hashmap.get(num) is None:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for num, count in hashmap.items():
            buckets[count].append(num)
        print(buckets)

        index = len(buckets) - 1
        while index >= 0 and len(result) < k:
            for item in buckets[index]:
                result.append(item)
            index -= 1
        
        return result
        