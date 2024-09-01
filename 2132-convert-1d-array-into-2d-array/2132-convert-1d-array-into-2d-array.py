class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if reshaping is possible
        if len(original) != m * n:
            return [] # Return an empty array if not possible
        
        # Fill the 2D array by slicing the original list
        return [original[i * n:(i + 1) * n] for i in range(m)]