class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        rp = len(people) - 1
        lp = 0
        boats = 0
        
        while lp <= rp:
            if people[lp] + people[rp] > limit:
                boats += 1
                rp -=1
            else:
                boats += 1
                rp -= 1
                lp += 1
        return boats