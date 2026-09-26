class Solution:
    def countSeniors(self, details: List[str]) -> int:
        number = 0
        for person in details:
            if int(person[11:13]) > 60:
                number = number + 1
        return number
            