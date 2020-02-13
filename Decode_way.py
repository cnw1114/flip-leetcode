class Solution: ## Time limit solution
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        string_key = [str(i) for i in range(1,27)]
        output = {} # iter:item
        
        for idx in range(len(s)):
            if not output:
                output[idx]=[[s[idx]]]
                continue
#             print(idx)
            output[idx] = []
            for elem in output[idx-1]:
                if elem[-1]+s[idx] in string_key:
                    elem_copy = elem[:]
                    elem_copy[-1] = elem_copy[-1]+s[idx]
                    s_merge = elem_copy
                    if not s_merge in output[idx]: #Memory에 저장 된 중복값을 제거
                        output[idx].append(s_merge)
                if s[idx]!='0':
                    s_append = elem + [s[idx]]
                    output[idx].append(s_append)

        return len(output[idx])
        
 class Solution:
    def numDecodings(self, s: str) -> int:
        last,c1,c2=int(s[0]),0 if not int(s[0]) else 1,0
        print(last,c1,c2)
        for i in s[1:]:
            now=int(i)
            if last==1 or last==2 :
                c1,c2,last=c1+c2 if now else 0,0 if last==2 and int(i)>6 else c1,now
            else:
                c1,c2,last=c1+c2 if now else 0,0,now
        return c1+c2
