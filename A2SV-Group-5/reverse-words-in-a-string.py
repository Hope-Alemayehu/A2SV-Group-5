class Solution:
    def reverseWords(self, s: str) -> str:
      reve=s.split()
      reve=reve[::-1]
      return " ".join(reve)