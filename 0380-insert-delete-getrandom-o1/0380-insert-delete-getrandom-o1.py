class RandomizedSet:

    def __init__(self): 
        self.num_index_map = defaultdict(int)
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.num_index_map:
            return False
        self.num_index_map[val] = len(self.values) 
        self.values.append(val)
        return True
       
    def remove(self, val: int) -> bool:
        if val not in self.num_index_map:
            return False
        val_index = self.num_index_map[val]
        last_val = self.values[-1]
        self.num_index_map[last_val] = val_index
        self.values[val_index] = last_val
        del(self.num_index_map[val])
        self.values.pop()

        return True
    def getRandom(self) -> int:
        
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()