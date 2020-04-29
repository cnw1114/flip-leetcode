from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lv = defaultdict(lambda: [])
        for level in range(numRows):
            lv[level]
        
        level = 0
        increase = True
        for st in s:
            if increase:
                lv[level].append(st)
                level += 1
                if level == numRows:
                    increase = False
                    level = numRows-1
            else:
                level -= 1
                lv[level].append(st)
                if level == 0:
                    increase = True
                    level = 1
        output = []
        for key in lv.keys():
            output+=lv[key]
            
        return ''.join(output)   
