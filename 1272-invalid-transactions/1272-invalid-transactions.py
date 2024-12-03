class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #time complexity O(NlogN + O(N*K))
        #space complexity O(N)
        parser = []
        n = len(transactions)
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            parser.append([name,int(time),int(amount),city, i])
        parser.sort(key=lambda x : (x[0],x[1]))
        invalid = set()
        for i, (name, time, amount, city, index) in enumerate(parser):
            if amount > 1000:
                invalid.add(index)
                
            for j in range(i-1,-1,-1):
                if parser[j][0] != name:
                    break
                if time - parser[j][1] > 60:
                    break
                if city != parser[j][3]:
                    invalid.add(index)
                    invalid.add(parser[j][4])
        result = []
        for idx in invalid:
            result.append(transactions[idx])
        return result
            
        
