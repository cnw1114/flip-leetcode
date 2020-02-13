class Solution: ## Time limit solution
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Memo_table = {}
        Memo_table[1] = wordDict
        idx=2
        while 1:
            tmp_out = []
            for elem1 in Memo_table[idx-1]:
                for elem2 in Memo_table[1]:
                    if elem1+elem2 in s:
                        tmp_out.append(elem1+elem2) 
            if not tmp_out:
                break
            Memo_table[idx] = tmp_out
            
            idx+=1
            
        print(Memo_table, idx)
        return s in Memo_table[idx-1]
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(s)):
            print(dp)
            if dp[i]:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict: # as in [i:j+1] it will take from i to j
                        dp[j+1] = True # as we made empty string as our zero position hence each increased by 1
        print(dp)
        return dp[-1]
