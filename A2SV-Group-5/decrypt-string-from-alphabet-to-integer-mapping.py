class Solution:
    def freqAlphabets(self, s: str) -> str:
        #create a hashmap 
        #keys: numbers
        #values are the letters
        the_map={"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h",
                    "9":"i","10":"j","11":"k","12":"l","13":"m","14":"n","15":"o",
                    "16":"p","17":"q","18":"r","19":"s","20":"t","21":"u","22":"v",
                    "23":"w","24":"x","25":"y","26":"z"}
        #iterate through the string
        res=""
        i=0
        while i<len(s):
            
            if i+2 <len(s) and s[i+2]=="#":
                res+=the_map[s[i:i+2]]
                #to skip the one we mapped already
                i+=3
            else:
                res+=the_map[s[i]]
                #to continue as normal
                i+=1
        return res