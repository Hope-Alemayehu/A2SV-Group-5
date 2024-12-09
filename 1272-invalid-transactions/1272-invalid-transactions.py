class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #build the hashmap name: [time, amount, index]
        nameMap = defaultdict(list)
        N = len(transactions)

        for i,t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            nameMap[name].append([int(time),int(amount),city,i])

        #create a list to store the invalid transaction indices
        invalidIndices = set()
        #iterate through each name.
        for key, value in nameMap.items():
            length = len(value)
            for i in range(length):
                if value[i][1] > 1000:
                    invalidIndices.add(value[i][3])
                    # continue
                for j in range(i+1,length):
                    if value[i][2] == value[j][2]:
                        continue
                    if abs(value[i][0] - value[j][0]) <= 60:
                        invalidIndices.add(value[i][3])
                        invalidIndices.add(value[j][3])
        # print(invalidIndices)               
        ans = []
        for i in invalidIndices:
            ans.append(transactions[i])

        return ans
