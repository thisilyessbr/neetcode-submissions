class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for s in strs :
          encoded_string += str(len(s))
          encoded_string += "#"
          encoded_string += s
        
        return encoded_string;




    def decode(self, s: str) -> List[str]:

        result = []

        i=0

        while i<len(s):

            j=s.index("#", i)
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            result.append(word)
            i+=length

        
        return result



