class Solution {
    public String removeVowels(String s) {
        String c = new String();
        String v = "aeiou";
        for (int i = 0; i < s.length(); i++)
        {
            if (v.indexOf(s.charAt(i)) == -1)
            {
                c = c + s.charAt(i);
            }
        }
        return c;
    }
}