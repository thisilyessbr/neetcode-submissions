class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        solution = {}
        for word in strs :
            key = "".join(sorted(word))
            solution.setdefault(key,[]).append(word)
        
        return list(solution.values())

