class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashi={}
        for i in range(len(names)):
            hashi[heights[i]]=names[i]
        
        
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if heights[i]<heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
       
        ans=[]
        for i in range(len(heights)):
            ans.append(hashi[heights[i]])
        return ans