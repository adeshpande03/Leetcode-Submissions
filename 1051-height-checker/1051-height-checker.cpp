class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> v = heights;
        int c = 0;
        sort(heights.begin(), heights.end());
        for (int i = 0; i < heights.size(); i++)
        {if (heights[i] != v[i]){c++;}}
        return c;
    }
};