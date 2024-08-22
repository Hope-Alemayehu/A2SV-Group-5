class Solution:
    def findComplement(self, num):
        # Convert the number to its binary representation and remove the "0b" prefix
        binary = bin(num)[2:]
        
        # Initialize an empty list to store the complement bits
        res = []
        
        # Iterate through each bit in the binary representation
        for b in binary:
            # Append the complement of each bit (0 -> 1, 1 -> 0)
            if b == "0":
                res.append("1")
            else:
                res.append("0")
        
        # Join the list of bits into a string and convert it back to a decimal number
        return int("".join(res), 2)