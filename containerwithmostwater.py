class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        length, output = len(height), 0
        
        for start in range(0, length-1):
            for end in range(start, length):
                w = end-start
                h = min(height[start], height[end])
                output = max(output, w*h)
        return output

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, left, right = 0, 0, len(height) - 1
        
        while left < right:
            area = max(area, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
