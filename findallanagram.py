from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        i, output, C_d, p_len, s_len = 0, [], Counter(p), len(p), len(s)
        while i+p_len != s_len+1:
            ana = s[i:i+p_len]
            if Counter(ana) == C_d:
                output.append(i)
            i+=1
        return output
