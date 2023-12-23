class Solution {
public:
    string removeTrailingZeros(string num) {
        if (num[num.length() - 1] != '0')
        {
            return num;
        }
        num.pop_back();
        return this->removeTrailingZeros(num);
        
    }
};