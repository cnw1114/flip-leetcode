class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cum = 0
        for idx, item in enumerate(nums):
            cum += item
            nums[idx] = cum
        else:
            del cum
        hash_t = {0:-1} # num 길이가 2짜리를 처리해주기 위해
        for idx, elem in enumerate(nums):
            if k:
                modular = elem%k
            else:
                modular = elem
            if modular in hash_t:
                if idx - hash_t[modular] >=2:
                    return True
                continue
            hash_t[modular]=idx
        return False
