class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i, item in enumerate(nums):
            value = hashmap.get(target - item)
            hashmap[item] = i
            if(value != None):
                result.append(value)
                result.append(i)
                return result
            