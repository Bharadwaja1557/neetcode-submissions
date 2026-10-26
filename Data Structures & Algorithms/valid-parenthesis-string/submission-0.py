class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = 0 # minmun number of "(" we can have
        openMax = 0 # maximum number of "(" we can have

        for c in s:
            if c == "(":
                openMin += 1
                openMax += 1
            elif c == ")":
                openMin -= 1
                openMax -= 1
            else:
                openMin -= 1
                openMax += 1
            
            if openMin < 0: # take example string   ( * ) ( 
                openMin = 0
            if openMax < 0:
                return False
        
        return openMin == 0 # this means every open bracket is closed