from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #time complexity O(N)
        #space complexity O(N)
        common = {}
        min_index_sum = float("inf")

        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                index_sum = i + list2.index(restaurant)

                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    common = {restaurant}
                elif index_sum == min_index_sum:
                    common.add(restaurant)

        return list(common)
