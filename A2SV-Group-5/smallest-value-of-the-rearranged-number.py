from functools import cmp_to_key

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        flag = False
        if num < 0:
            flag = True
        num = abs(num)
        
        lst = []
        while num > 0:
            lst.append(str(num % 10))
            num = num // 10
        
        lst = lst[::-1]

        def first(n1, n2):  # this is if num is negative numbers
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        def second(n1, n2):  # for the positive numbers
            if n1 + n2 > n2 + n1:
                return 1
            else:
                return -1

        if flag:
            ans = sorted(lst, key=cmp_to_key(first))
            res = 0 - int("".join(ans))
            return res
        else:
            ans = sorted(lst, key=cmp_to_key(second))

            # Move the zero to the first index
            if ans[0] == "0":
                for i in range(1, len(ans)):
                    if ans[i] != "0":
                        ans[0], ans[i] = ans[i], ans[0]
                        break

            return int("".join(ans))

