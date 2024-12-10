class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # transactions.sort()
        parser = []
        for i,transaction in enumerate(transactions):
            name,time, amount, city = transaction.split(",")
            parser.append([name, int(time),int(amount),city,i])

        parser.sort(key=lambda x:(x[0],x[1]))
        invalids = set()
        for index, value in enumerate(parser):
            name, time, amount, city, i = value
            if amount > 1000:
                invalids.add(i)
            for j in range (index-1,-1,-1):
                if name != parser[j][0]:
                    break
                if (time - parser[j][1]) > 60:
                    break
                if city != parser[j][3]:
                    invalids.add(i)
                    invalids.add(parser[j][4])
        results = []
        # print(invalids)
        for i in invalids:
            results.append(transactions[i])
        return results
        # [[ali,20,100,bej],[alic,40,122,bej],[ali,50,214,ny]]