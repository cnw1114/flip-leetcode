class Solution: #Recursion
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            a = self.subsets(nums[1:])
        return a + [[nums[0]]+a_item for a_item in a]

class Solution: #DP
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for item in nums:
            subset += [elem + [item] for elem in subset]
        return subset
