class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        res = score = 0
        tokens.sort()
        
        l,r = 0 , len(tokens)-1
        while l<=r:
            if power >=tokens[l]: # face up cuz you can play all the small toens in the List
                power -= tokens[l]
                l+=1
                score+=1
                res = max(res,score)
            elif score > 0: # if you have a score but not have power then from the right face down
                power +=tokens[r]
                r-=1
                score -=1
            else: # you stuck with 0 and 0 power and score so break and return 
                break
        return res