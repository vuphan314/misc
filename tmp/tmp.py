class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        if n == 2:
            return max(heights[0], heights[1], 2 * min(heights))
        else:
            return max(
                self.largestRectangleArea(heights[:-1]),
                heights[-1],
!
            )
