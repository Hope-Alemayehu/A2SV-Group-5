class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]* len(s)
        n = len(s)
        characters = []

        #construct the array that will help us construct the prefix sum 
        for i in range(len(shifts)):
            l = shifts[i][0]
            r = shifts[i][1]
            val =shifts[i][2]

            if val == 0:
                arr [l] -= 1
                if r + 1 < n:
                    arr[r + 1] += 1
            else:
                arr [l] += 1
                if r + 1 < n:
                    arr[r + 1] -= 1
       
        #calculating the prefix sum from the array
        for i in range(1,n):
            arr[i] += arr[i-1]

        #to finally get the charcter after applying the shift
        res = []

        print(arr)

        for i ,c in enumerate(s):
            shifts = arr[i] % 26
            if (ord(c) + shifts) > ord("z"):
                res.append(chr(ord("a") + (shifts - (ord("z") - ord(c))) - 1))
            else:
                res.append(chr(ord(c) + shifts))
           
        return "".join(res)

        

