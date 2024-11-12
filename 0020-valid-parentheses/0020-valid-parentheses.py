class Solution:
    def isValid(self, s: str) -> bool:
        #time complexity O(N)
        #time complexity O(N) + O(3) ~ O(N)
        #create a stack
        stack = []
        #create a map that connect the opening and closing brackets
        bracket_pairs = {")":"(", "]":"[","}":"{"}

        #iterate through the string
        for char in s:
            #check if the stack isn't empty 
            #the last element is the opeing bracket of current string
            if stack and char in bracket_pairs and bracket_pairs[char] == stack[-1]:
                stack.pop()
                continue
            #if not we append it to the stack to find its partner
            stack.append(char)
        return len(stack) == 0
    