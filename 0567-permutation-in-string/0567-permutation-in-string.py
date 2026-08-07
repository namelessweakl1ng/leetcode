class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1count, s2count = [0]*26 ,[0]*26 # maek array of length 26 of each number 26
        matches = 0 # make a variable to match the both s1 and s2
        for i in range(len(s1)): # increment the number of character apperance on the window in this case this case its len(s1)
            s1count[ord(s1[i]) - ord('a')]+=1
            s2count[ord(s2[i]) - ord('a')]+=1
        for i in range(26): # got throught every index in the s1 and s2 and then if they matches inceremtn the matches
            matches += 1 if s1count[i]==s2count[i] else 0 
        l=0 # left pointer
        for r in range(len(s1),len(s2)): # already assigned the first window so start from the len(s1) which is non inclusive
            if matches ==26: return True # if it already matching then return true meaning if the first window matches
            index = ord(s2[r]) - ord('a') # declare the index performing the ord gives us the index meaning we subtracting the ascii
            s2count[index] +=1 # increment what you see in the window
            if s1count[index]==s2count[index]: # right now the matches can be like 23, 24,25 or anything if and elif statement helps
                matches+=1 #to change the thing until it reaches the 26
            elif s1count[index] + 1 ==s2count[index]:# Or did it stop being equal?
                matches-=1
            index = ord(s2[l]) - ord('a')
            s2count[index] -=1
            if s1count[index]==s2count[index]: # is it equal orr
                matches+=1
            elif s1count[index] - 1 ==s2count[index]: # Or did it stop being equal?
                matches-=1
            l+=1 #move the left pointer
        return matches ==26 # at the last window we dont have a conditon to check weather the matches is 26 so we return the bool