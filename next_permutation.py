class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for right_idx in range(len(nums)-1,0, -1):
            if nums[right_idx -1] < nums[right_idx]:
                if right_idx == len(nums)-1:
                    nums[right_idx - 1], nums[right_idx] = nums[right_idx], nums[right_idx - 1]
                    return 
                else:
                    for right_idx_upper in range(len(nums)-1,right_idx-1, -1):
                        if nums[right_idx_upper] > nums[right_idx-1]:
                            break
                    nums[right_idx-1], nums[right_idx_upper] = nums[right_idx_upper], nums[right_idx-1]
                    nums[right_idx:] = nums[right_idx:][::-1]
                    return
        nums.reverse()
        return
