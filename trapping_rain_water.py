from collections import Counter
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0 or len(height)==1:
            return 0

        max_heigth = max(height)
        output = 0
        temp_item = []
        for _ in range(max_heigth):
            for item in height:
                temp_item.append(item-1)
            temp_output = Counter(temp_item)[-1]
            
            right_side = 0
            if temp_item[-1] == -1: ## 가장 우측 안 담기는 공간을 파악
                for elem in temp_item[::-1]:
                    if elem != -1:
                        break
                    right_side -= 1
                    
            left_side = 0
            if temp_item[0] == -1: ## 가장 좌측 안 담기는 공간을 파악
                for elem in temp_item:
                    if elem != -1:
                        break
                    left_side -= 1

            temp_output = temp_output + left_side + right_side ## 높이의 level별 갇힌 물의 수
            
            for idx, item in enumerate(temp_item):
                height[idx] = item if item != -1 else 0 ## -1인 부분을 0으로 만들어서 진행
            temp_item = []
            
            output += temp_output
        
        return output
