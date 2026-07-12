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
            result.append(s[index:index+length_of_word])
            index += length_of_word
            
        return result
        
           
