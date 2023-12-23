class Solution {
public:
    string removeTrailingZeros(string num) {
        while (1)
        {
        if (num[num.length() - 1] != '0')
        {
            return num;
        }
        num.pop_back();
        
        }
    }
};