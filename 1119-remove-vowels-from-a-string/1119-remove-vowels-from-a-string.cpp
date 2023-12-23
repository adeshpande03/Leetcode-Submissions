class Solution {
public:
    string removeVowels(string s) {
    string ans;
    set<char> vowels {'a', 'e', 'i', 'o', 'u'};
    for (auto c : s)
        if (vowels.find(c) == vowels.end())
            ans += c;
    return ans;
}
};