class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        h1, m1 = map(int, loginTime.split(':'))
        h2, m2 = map(int, logoutTime.split(':'))
        
        if 0 <= (h2*60 + m2 - (h1*60 + m1)) < 15:
            return 0
        
        while m1 % 15:
            m1 += 1
        
        if m1 == 60:
            m1 = 0
            h1 = (h1 + 1) % 24
     
        while m2 % 15:
            m2 -= 1
        
        minutes_played = (h2-h1) * 60 + (m2-m1)
        if minutes_played < 0:
            minutes_played += 24 * 60 

        return minutes_played // 15