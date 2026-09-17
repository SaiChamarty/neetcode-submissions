class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left = 0
        right = len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] < target:
                left = left + 1
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                result.append(left+1)
                result.append(right+1)
                return result
                
