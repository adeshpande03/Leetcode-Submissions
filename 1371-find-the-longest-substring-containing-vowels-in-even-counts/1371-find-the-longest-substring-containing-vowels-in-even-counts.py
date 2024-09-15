class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        bitmask_position = {0: -1} 
        current_bitmask = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowels:
                current_bitmask ^= (1 << vowels[char])
            
            if current_bitmask in bitmask_position:
                max_length = max(max_length, i - bitmask_position[current_bitmask])
            else:
                bitmask_position[current_bitmask] = i
        
        return max_length