impl Solution {
    pub fn remove_vowels(s: String) -> String {
        let mut ans = String::new();
        for x in s.chars()
        {
            if x != 'a' && x != 'e' && x != 'i' && x != 'o' && x != 'u'
            {
                ans.push(x);
            }
        }
        ans
    }
}