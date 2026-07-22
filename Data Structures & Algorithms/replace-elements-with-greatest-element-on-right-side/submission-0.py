class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = 0
        ans = [0]*len(arr)
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                curr_max = arr[i]
                ans[i] = -1
            else:
                ans[i] = curr_max
                curr_max = max(arr[i], curr_max)
        return ans
