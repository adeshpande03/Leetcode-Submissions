class Solution {
public:
    int countOperations(int num1, int num2) {
        int d = 0;
        while(num1 > 0 && num2 > 0)
        {
            if (num1 < num2)
            {
                int c = num1;
                num1 = num2;
                num2 = c;
            }
            num1 -= num2;
            d += 1;
        }
        return d;
    }
};