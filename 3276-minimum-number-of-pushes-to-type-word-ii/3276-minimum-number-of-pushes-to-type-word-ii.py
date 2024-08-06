class Solution:
    def minimumPushes(self, word: str) -> int:
        charCount = Counter(word)
        # print(charCount)
        arr = list(charCount.values())
        arr.sort(reverse = True)
        # print(arr)

        res = 0
        multiplier = 1
        for i in range(len(arr)): 
            res += (multiplier * arr[i])
            # print(res)
            if (i + 1) % 8 == 0:
                multiplier += 1
        return res