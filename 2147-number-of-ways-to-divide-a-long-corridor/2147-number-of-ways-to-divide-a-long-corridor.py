class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        coorridor_seats = [i for i in range(n) if corridor[i] == "S"]
        number_of_seats = len(coorridor_seats)
        if number_of_seats % 2 != 0 or number_of_seats   == 0:
            return 0
        
        space = 1
        for j in range(0, len(coorridor_seats) -1):
            if j %2 != 0:
                end = coorridor_seats[j]
                start = coorridor_seats[j+1]
                space *= (start-end)
        return space % (10**9 + 7)