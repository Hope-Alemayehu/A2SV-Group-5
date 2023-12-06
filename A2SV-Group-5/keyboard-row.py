class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        ans=[]
        rows=[set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]

        for word in words:
            lower_word=set(word.lower())

            for row in rows:
                if lower_word <= row:
                    ans.append(word)
        return ans
        