#Time limit error solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s)==2:
            if s[0] != s[1]:
                return s[0]
            else:
                return s
        if len(set(s))==1:
            return s
        
        palin_table = {}
        
        for idx, item in enumerate(s):
            palin_table[(idx,)] = item

        breakit_list = []
        count = 0
        while True:
            count+=1
            breakit_list = list(palin_table.keys())

            for key in breakit_list:
                if int(key[0])==0:
                    continue
                if len(key)==1:
                    if palin_table[(key[0]-1,)] == palin_table[key]:
                        palin_table[(key[0]-1,)+key] = palin_table[(key[0]-1,)] + palin_table[key]
                        
                        try:
                            if palin_table[(key[0]-1,)] == palin_table[(key[-1]+1,)]:
                                palin_table[(key[0]-1,) + key + (key[-1]+1,)] = palin_table[(key[0]-1,)] + palin_table[key] + palin_table[(key[-1]+1,)]
                        except:
                            pass
                        
                    elif key[0] == len(s)-1:
                        pass
                    elif palin_table[(key[0]-1,)] == palin_table[(key[0]+1,)]:
                        palin_table[(key[0]-1,)+key+(key[0]+1,)] = palin_table[(key[0]-1,)] + palin_table[key] + palin_table[(key[0]+1,)]
                
                else:
                    if key[0]!='0' and key[-1]!=str(len(s)-1):
                        if len(s)<len(key):
                            break
                        try:
                            if palin_table[(key[0]-1,)] == palin_table[(key[-1]+1,)]:
                                palin_table[(key[0]-1,) + key + (key[-1]+1,)] = palin_table[(key[0]-1,)] + palin_table[key] + palin_table[(key[-1]+1,)]
                        except:
                            pass
            
            if breakit_list == list(palin_table.keys()):
                break
            else:
                breakit_list = palin_table.keys()

        return palin_table[max(palin_table.keys(),key=len)]
        
#O(N^2) solution========================
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
