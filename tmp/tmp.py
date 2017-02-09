import matplotlib.pyplot as pp
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        rectangle = rectangles[0]
        totalArea = self.getArea(rectangle)
        leftMost, bottomMost, rightMost, topMost = rectangle
        leftSet = {0}
        bottomSet = {0}
        rightSet = {0}
        topSet = {0}
        for i in range(1, len(rectangles)):
            thisRectangle = rectangles[i]
            totalArea += self.getArea(thisRectangle)
            thisLeft, thisBottom, thisRight, thisTop = thisRectangle
            if thisLeft == leftMost:
                leftSet.add(i)
            if thisLeft < leftMost:
                leftSet = {i}
                leftMost = thisLeft
            if thisBottom == bottomMost:
                bottomSet.add(i)
            if thisBottom < bottomMost:
                bottomSet = {i}
                bottomMost = thisBottom
            if thisRight == rightMost:
                rightSet.add(i)
            if thisRight > rightMost:
                rightSet = {i}
                rightMost = thisRight
            if thisTop == topMost:
                topSet.add(i)
            if thisTop > topMost:
                topSet = {i}
                topMost = thisTop
        cornerSets = leftSet & bottomSet, leftSet & topSet, rightSet & bottomSet, rightSet & topSet
        for cornerSet in cornerSets:
            if len(cornerSet) != 1:
                return False
        superRectangle = [leftMost, bottomMost, rightMost, topMost]
        superArea = self.getArea(superRectangle)
        self.plotRectangle(superRectangle)
        return totalArea == superArea
    def getArea(self, rectangle):
        l, b, r, t = rectangle
        return (r - l) * (t - b)
    def plotRectangle(self, rectangle):
        l, b, r, t = rectangle
        pp.scatter(l, b)
        pp.scatter(r, t)
        pp.grid()
        pp.show()
############################################################
import unittest
class Test(unittest.TestCase):
    def test(self):
        f = Solution().isRectangleCover
        inputs = [
            [
                [1,1,3,3],
                [3,1,4,2],
                [3,2,4,4],
                [1,3,2,4],
                [2,3,3,4]
            ],
            [
                [1,1,2,3],
                [1,3,2,4],
                [3,1,4,2],
                [3,2,4,4]
            ],
            [
                [1,1,3,3],
                [3,1,4,2],
                [1,3,2,4],
                [3,2,4,4]
            ],
            [
                [1,1,3,3],
                [3,1,4,2],
                [1,3,2,4],
                [2,2,4,4]
            ],
            [[0,0,1,1],[0,1,3,2],[1,0,2,2]],
            [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]
        ]
        expected_outputs = [
            True,
            False,
            False,
            False,
            False,
            False
        ]
        n = len(inputs)
        for i in range(n - 1, n):
            returned_output = f(inputs[i])
            self.assertEqual(returned_output, expected_outputs[i])
if __name__ == '__main__':
    pass
    unittest.main()
