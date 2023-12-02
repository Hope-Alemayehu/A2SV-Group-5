class Solution:
    def romanToInt(self, s: str) -> int:
        hashi={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        le=len(s)
        for i in range(le):
            if i+1<le and hashi[s[i]]<hashi[s[i+1]]:
                res-=hashi[s[i]]
            elif  i+1<le and hashi[s[i]]>=hashi[s[i+1]]:
                res+=hashi[s[i]]
            if i==le-1:
                res+=hashi[s[i]]
        return res