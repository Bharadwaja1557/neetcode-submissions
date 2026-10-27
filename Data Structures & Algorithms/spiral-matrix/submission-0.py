class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        # remember that "right" and "bottom" are out of bounds

        while left < right and top < bottom:
            # get every element in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every element in right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            
            right -= 1

            # dont forget about one row matrices like   [1, 5, 5, 7]
            if not (left < right and top < bottom):
                break
            
            # get every element in bottom row in reverse order
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            
            bottom -= 1
            
            # get every element in left column in reverse order
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            
            left += 1
    
        return res