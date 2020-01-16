class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        answer = False
        count_val = 0
        
        max_loop_length = 15
        temp = 0
        while count_val != 1 and temp <= max_loop_length:
            temp += 1
            
            for i in s:
                count_val += eval(i)**2
            if count_val == 1:
                return True
            s = str(count_val)
            count_val = 0
        
        return answer
