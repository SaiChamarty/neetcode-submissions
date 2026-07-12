class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        result = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            # look if the sorted string has a key in grouped already:
            value = grouped.get(sorted_string)
            # if value == None, create a new list
            # add that sorted string's new list to grouped
            if value == None:
                li = []
                li.append(string)
                grouped[sorted_string] = li
            else:
                # append a new string to the list
                grouped[sorted_string].append(string)

        for item in grouped:
            result.append(grouped[item])
        return result