#include <iostream>
#include <set>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int>& bars ();
    int numBars;
    vector<int>& sortedHeights ();
    int largestRectangleArea(vector<int>& heights) {
        vector<int>& bars = heights;
        numBars = bars.size();
        set<int> s (bars.begin(), bars.end());
        sortedHeights.assign(s.begin(), s.end());
        int maxArea = 0;
        for (int barIndex = 0; barIndex < numBars; barIndex++) {
            int maxAreaFromBarIndex = getMaxAreaFromBarIndex(barIndex);
            if (maxAreaFromBarIndex > maxArea) {
                maxArea = maxAreaFromBarIndex;
            }
        }
        return maxArea;
    }
    int getMaxAreaFromBarIndex(int barIndex) {
        int barHeight = bars.at(barIndex);
        int currentMaxArea = 0;
        for (int i = 0; i < sortedHeights.size(); i++) {
            int currentHeight = sortedHeights[i];
            if (currentHeight > barHeight) {
                break;
            } else {
                int maxAreaFromBarIndexAndCurrentHeight = getMaxAreaFromBarIndexAndCurrentHeight(barIndex, currentHeight);
                if (maxAreaFromBarIndexAndCurrentHeight > currentMaxArea) {
                currentMaxArea = maxAreaFromBarIndexAndCurrentHeight;
                }
            }
        }
        return currentMaxArea;
    }
    int getMaxAreaFromBarIndexAndCurrentHeight(int barIndex, int currentHeight) {
        int currentIndex = barIndex;
        while (currentIndex < numBars && bars[currentIndex] >= currentHeight) {
            currentIndex++;
        }
        int baseLength = currentIndex - barIndex;
        return currentHeight * baseLength;
    }
};
int main() {
    Solution solution = new Solution();
    vector<int>& input = {1, 2};
    int output = 2;
    int maxArea = solution.largestRectangleArea(input);
    cout << maxArea;
}
