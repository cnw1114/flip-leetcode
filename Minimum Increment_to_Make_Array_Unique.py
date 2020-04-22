from collections import Counter

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        
        min_v, max_v, count_v = min(A), max(A), Counter(A)
        dupl_elem = []

        for elem in range(min_v, max_v+1):
            if count_v[elem] != 1:
                temp = [elem]*(count_v[elem]-1)
                dupl_elem += temp
                
        dupl_elem = sorted(dupl_elem) ## 작은 것 부터 채우기 위해
        
        output = 0
        cur_v = min_v
        while dupl_elem:
            if count_v[cur_v] == 0:
                item = dupl_elem.pop(0)
                if item > cur_v: ## 줄어드는 경우를 방지
                    ## 다시 중복을 넣을 때, 가장 작은 값이므로 0번째에다가 삽입
                    dupl_elem.insert(0, item) 
                    cur_v += 1
                    continue
                increment = cur_v - item
                output += increment
            cur_v += 1
        
        return output
