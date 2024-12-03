class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        nameMap = defaultdict(list)
        
        for i in range(len(transactions)):
            name,time,amount,city = transactions[i].split(",")
            if int(amount) > 1000:
                invalid.add(i)
            
            for prevtime, prevcity, index in nameMap[name]:
                if  abs(prevtime - int(time)) <= 60 and prevcity != city:
                    invalid.add(i)
                    invalid.add(index)
            nameMap[name].append([int(time),city,i])

        result = []
        for index in invalid:
            result.append(transactions[index])
        return result