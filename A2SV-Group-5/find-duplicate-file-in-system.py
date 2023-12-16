class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #to understand this problem we have paths of directory info
        #we need to return the duplicate files meaning they occured more than once in the file
# "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
        #time complexity O(N^2)
        #space complexity O(N)

        #dictionary to keep count of the occurence
        c=defaultdict(list)
        #to split the paths by the space

        for path in paths:
            
            path=path.split(" ")
            folder=path[0]
            
            
            #to store the splited string inside the 
            for s in path[1:]:
                #im gonna split it by .txt to get the file name and path
                s=s.split(".txt")
                
                name=s[0]
                content=s[1]
                c[content].append((folder, name))

        
        #to find those that are repeated
        output=[]

        for key,val in c.items():
            if len(val)>1:
                temp=[]
                for way,name in val:
                    temp.append(way+"/"+name+".txt")
                output.append(temp)
        return output
