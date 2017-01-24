import unittest
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        self.bars = heights
        self.numBars = len(self.bars)
        self.sortedHeights = sorted(set(self.bars))
        self.maxArea = 0
        for barIndex in range(numBars):
            self.maxArea = max(
                self.maxArea,
                self.getMaxAreaFromBarIndex(barIndex)
            )
        return self.maxArea
    def getMaxAreaFromBarIndex(self, barIndex):
        barHeight = self.bars[barIndex]
        currentMaxArea = 0
        for currentHeight in self.sortedHeights:
            if currentHeight > barHeight:
                break
            else:
                currentMaxArea = max(
                    currentMaxArea,
                    self.getMaxAreaFromBarIndexAndCurrentHeight(
                        barIndex, currentHeight
                    )
                )
        return currentMaxArea
    def getMaxAreaFromBarIndexAndCurrentHeight(
        self, barIndex, currentHeight
    ):
        currentIndex = barIndex
        while (
            currentIndex < self.numBars and
            self.bars[currentIndex] <= currentHeight
        ):
            currentIndex += 1
        baseLength = currentIndex - barIndex
        return currentHeight * baseLength
class Test(unittest.TestCase):
    def test(self):
        heights = [2,1,5,6,2,3]
        maxArea = Solution.largestRectangleArea(heights)
        self.assertEqual(maxArea, 10)
if __name__ == '__main__':
    unittest.main()
