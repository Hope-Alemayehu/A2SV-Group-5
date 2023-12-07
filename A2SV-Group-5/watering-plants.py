class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
    
        '''
            [2,2,3,4] capacity = 5
            plant 0 takes 2 -capacity = 3 step 1
            plant 1 takes 2 -capacity = 1 step =2
            plant 2 need 3 capacity=1 so to refill walk to the last last step =2
                        walk back= step 3 capacity=1+3=4 after watering capacity=2
            plant 3 needs 3 and capacity=


        '''
        ans=0
        curcapacity =0

        for i,plant in enumerate(plants):
            if curcapacity +plant<=capacity:
                curcapacity+=plant
            else:
                curcapacity =plant #to reset
                ans+=i*2
        return ans+ len(plants)



