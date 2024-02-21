class Solution:
    def getRow(self, n: int) -> List[int]:
        #this should work
        #im
        result = []
      
        def triangle(n):
            
            if n == 0:
                return []
            elif n == 1:
                return [1]
            else:
                newRow = [1]
                result = triangle(n-1)
                lastRow = result
                for i in range(len(lastRow)-1):
                    newRow.append(lastRow[i] + lastRow[i+1])
                newRow += [1]

                #print(newRow)
                result.append(newRow)
                # print(result)
                return result[-1]
        return triangle(n+1)