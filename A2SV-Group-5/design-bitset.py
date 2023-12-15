class Bitset:

    def __init__(self, size: int):
        #to store the original bits True->1 and False->0
        self.bit=[False for i in range(size)]

        #inver the list of self.bit
        self.bitinv=[True for i in range(size)]

        #counter for True
        self.ones=0

        #counter for False
        self.zeros=size

        #original size\
        self.size=size

    def fix(self, idx: int) -> None:
        
        #if zero it updates it to one
        if not self.bit[idx]:
            self.zeros-=1
            self.ones+=1
        self.bit[idx]=True
        self.bitinv[idx]=False

    def unfix(self, idx: int) -> None:
        #if the bitis set to one we change it to zero
        if self.bit[idx]:
            self.zeros+=1
            self.ones-=1
        self.bit[idx]=False
        self.bitinv[idx]=True



    def flip(self) -> None:
        self.ones,self.zeros=self.zeros,self.ones
        self.bit,self.bitinv=self.bitinv,self.bit

    def all(self) -> bool:
        return self.ones==self.size
    

    def one(self) -> bool:
        return self.ones>0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        
        ans=""
        for bit in self.bit:
            if bit:
                ans+='1'
            else:
                ans+='0'
        return ans

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()