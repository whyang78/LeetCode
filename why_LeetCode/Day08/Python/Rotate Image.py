//竖着中线反转，然后转置
class Solution:
    def rotate(self, matrix):  
        matrix[:] = map(list,zip(*matrix[::-1]))  