from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        #if nothing there in the strings
        if not s or not t:
            return ""
        #declarea variables c
        # count creates a dict like {A:1 , B:1, C:1}
        need = Counter(t)
        left = end = start =0
        missing = len(t)
        for right,ch in enumerate(s,1):
            if need[ch]>0:
                #if the element we need exist in the window then reduce the missing
                missing-=1
            #keep decreasin the value of the dict for every element you see until the missing becomes 0
            need[ch]-=1
            while missing==0:
                #this gives us the minimum window
                if end ==0 or right - left < end - start:
                    start, end = left,right
                #start redcing the window from the left
                need[s[left]]+=1
                #IF THERE IS A NEED for a character then increase the missing
                if need[s[left]]>0:
                    missing+=1
                #increment the left so that we can dynamically increase and decrease the windows size 
                # so that all the elements fit in the window
                left+=1
        return s[start:end]