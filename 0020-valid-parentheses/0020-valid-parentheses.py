class Solution:
    def isValid(self, s: str) -> bool:
        #time complexity O(N)
        #time complexity O(N) + O(3) ~ O(N)
        #create a stack
        stack = []
        #create a map that connect the opening and closing brackets
        bracket_map = {")":"(", "]":"[","}":"{"}

        #iterate through the string
        N = len(s)
        for i in range(N):
            #check if the stack isn't empty 
            #the last element is the opeing bracket of current string
            if stack and s[i] in bracket_map and bracket_map[s[i]] == stack[-1]:
                #if that's the case pop it 
                stack.pop()
                continue
            #if not we append it to the stack to find its partner
            stack.append(s[i])
        return len(stack) == 0
    