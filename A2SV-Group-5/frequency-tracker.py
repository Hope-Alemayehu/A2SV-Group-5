class FrequencyTracker:

    def __init__(self):
        self.freq=defaultdict(int)
        self.values = defaultdict(int)

    def add(self, number: int) -> None:
        self.values[self.freq[number]] -= 1
        self.freq[number]+=1
        self.values[self.freq[number]] += 1


    def deleteOne(self, number: int) -> None:
        if self.freq[number]!=0:
            self.values[self.freq[number]] -= 1
            self.freq[number]-=1
            self.values[self.freq[number]] += 1


    def hasFrequency(self, frequency: int) -> bool:
        if self.values[frequency] > 0:
            return True
        return False



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)