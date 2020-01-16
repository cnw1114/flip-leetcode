class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict = dict()
        start = max_length = 0
        for position_idx, item in enumerate(s):
            if item in str_dict:
                temp_start = str_dict[item] + 1
                if temp_start > start: ## 'abba'같은 것을 처리 못한다. a가 0 index에 있으므로 start 포인트가 뒤로 가기 때문에 reasonable 하지 않음
                    start = temp_start
            temp_length = position_idx - start + 1
            if max_length < temp_length: #subseq 중 가장 긴 것을 반환하기 위해서
                max_length = temp_length
            str_dict[item] = position_idx
        
        return max_length
