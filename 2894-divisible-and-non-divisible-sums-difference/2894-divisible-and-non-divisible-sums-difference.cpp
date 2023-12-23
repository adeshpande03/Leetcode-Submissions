class Solution {
public:
    int differenceOfSums(int n, int m) {
        int c = 0;
        int d = 0;
        for (int i = 1; i <= n; i++)
        {
            if (i % m == 0)
            {
                d += i;
            }
            else
            {
                c += i;
            }
        }
        return c - d;
    }
};