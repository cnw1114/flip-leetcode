class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        Memo_table = dict()
        Memo_table[0] = []
        
        for idx, item in enumerate(nums):
            if not Memo_table[idx]:
                Memo_table[idx+1] = [[item]]
                continue
            temp_output = []
            for elem in Memo_table[idx]:
                for elem_idx in range(len(elem)+1):
                    copy_elem = elem[:] ## list copy
                    copy_elem.insert(elem_idx,item)
                    temp_output.append(copy_elem)
                Memo_table[idx+1] = temp_output
        return Memo_table[len(nums)]
