class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        order = {}

        for word in strs:
            key = "".join(sorted(word))
            order.setdefault(key,[]).append(word)

        return list(order.values())
            