class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        num_words = len(strs)
        result.append(str(num_words) + "#")
        for item in strs:
            length = str(len(item))
            result.append(length)
            result.append("#")
            result.append(item)
        answer = "".join(result)
        return answer

    def decode(self, s: str) -> List[str]:
        result = []
        current_str = []
        index = 0
        while s[index] != "#":
            index += 1
        num_words = int(s[0:index])
        print(num_words)
        print(s)
        index+=1
        for i in range(num_words):
            temp = index
            separator = s[temp]
            while separator != "#":
                temp += 1
                separator = s[temp]
            length_of_word = int(s[index:temp])
            index = temp + 1
            for char in range(index, index + length_of_word):
                current_str.append(s[char])
                index += 1
            result.append("".join(current_str))
            current_str = []
            
        return result
        
           
