class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        rp = len(people) - 1
        lp = 0
        boats = 0
        
        while lp <= rp:
            boats += 1
            if people[lp] + people[rp] > limit:
                rp -=1
            else:
                rp -= 1
                lp += 1
        return boats