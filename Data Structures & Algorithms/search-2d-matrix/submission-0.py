class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list_matrix = []
        for i in matrix:
            list_matrix += i
        print(list_matrix)
        left = 0
        right = len(list_matrix)
        while left < right:
            mid = (left + right) // 2
            if list_matrix[mid] > target:
                right = mid
            elif list_matrix[mid] < target:
                left = mid + 1
            elif list_matrix[mid] == target:
                return True
        return False
