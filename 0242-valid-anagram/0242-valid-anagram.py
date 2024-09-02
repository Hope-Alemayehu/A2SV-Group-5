class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we can sort them and check if they are equal
        #time complexity would be O(NlogN) however we can do this in O(N)

        return Counter(s) == Counter(t)