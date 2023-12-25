class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        hashi = defaultdict(list)
        for i in range(len(boxes)):
            if boxes[i]=="0":
                hashi[0].append(i)
            else:
                hashi[1].append(i)
        values = hashi[1]
        
        res=[]
        for i in range(len(boxes)):
            count=0

            for j in range(len(values)):
                temp=abs(i-values[j])
                count+=temp
            res.append(count)
        return res
            
