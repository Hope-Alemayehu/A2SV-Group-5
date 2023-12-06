class Solution:
    def totalMoney(self, n: int) -> int:
        #he puts money every day
        #the first monday will be 1
        #every day he add to the saving the day before
        #the next monday = first monday + 1

        save=0
        day=0
        deposit=1

        while day<n:
            save+=deposit
            
            deposit+=1
            day+=1
            #to check if the day has entered the  next week and update 
            #the day accordingly
            if day%7==0:
                deposit =1+day//7
        return save