class Solution(object):
    def totalFruit(self, fruits):
        l = res = total = 0
        count = collections.defaultdict(int) # dfault dict so that i dont have to manually pu the numbers in the hashmap
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total +=1
            while len(count)>2:
                count[fruits[l]]-=1
                total -=1
                if not count[fruits[l]]: # reordered this so that it pops before incrementing
                    count.pop(fruits[l])
                l+=1
            res = max(res,total)
        return res