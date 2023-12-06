class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #time complexity O(N^2)
        #space complexity O(1)
        
        #we are looking for the first different characters
        #if word A is prefix of word B ,word B must come after the word A since it is longer

        #creating a dictionary to map the index of the order
        #c is the character (key),i (value) is the index that character is found
        orderInd={c:i for i ,c in enumerate(order)}

        #comparing per pair
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]

            for j in range(len(w1)):
                if j== len(w2):
                    return False
                #chaecking the different characters of the two words
                if w1[j]!=w2[j]:
                    if orderInd[w1[j]]>orderInd[w2[j]]:
                        return False
                    #if that didn't happen it means they are in order so we break out of this loop to compare the rest of the words
                    break
        return True
