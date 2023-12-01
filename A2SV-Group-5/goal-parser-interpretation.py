class Solution:
    def interpret(self, command: str) -> str:
        #time complexity O(n)
        #space complexity O(n)
        #approch: two pointers

        l=0
        r=1
        n=len(command)
        s=""
        while l<r and r<n+1:
            if command[l]=="G":
                s+="G"
                r+=1
                l=r-1
             
            elif command[l]=="(" and command[r]==")":
                s+="o"
                r+=2
                l=r-1
            elif command[l]=='(' and command[r]=="a":
                s+="al"
                r=r+4
                l=r-1
        return s
            


      
