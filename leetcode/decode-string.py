class Solution:
    def decodeString(self, s: str) -> str:

        def rec(idx):
            result = []
            k = 0

            while idx < len(s):
                if s[idx].isdigit():
                    k = k * 10 + int(s[idx])

                elif s[idx] == '[':
                    idx, decoded = rec(idx + 1)
                    result.append(k * decoded)
                    k = 0

                elif s[idx] == ']':
                    return idx, "".join(result)

                else:
                    result.append(s[idx])

                idx += 1

            return idx, "".join(result)

        return rec(0)[1]