class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
      
        if n==3:
            return salary[1]
        elif n>3:
            summ=sum(salary[1:n-1])
            return summ/(n-2)