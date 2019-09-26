//其实此方法不行，无法in-place
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy
        matrix=numpy.array(matrix)
        rows,columns=numpy.where(matrix==0)
        matrix[rows,:]=0
        matrix[:,columns]=0
        matrix=list(matrix)