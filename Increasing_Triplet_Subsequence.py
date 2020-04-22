class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if not nums or len(nums)<3:
            return False
        
        low = mid = None
        for elem in nums:
            if mid != None and elem > mid:
                return True
            if low == None or elem < low:
                low = elem
            elif low != None and elem > low:
                mid = elem

        
        return False
