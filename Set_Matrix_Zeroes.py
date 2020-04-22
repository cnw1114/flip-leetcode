class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        col_zero = []
        for row, list_ in enumerate(matrix):
            for col, elem in enumerate(list_):
                if elem == 0: 
                    col_zero.append(col) ## zero를 포함한 column 인덱스를 저장
                    matrix[row] = [0]*len(list_) ## zero를 포함한 list 모조리 zero로 만들기
        
        ## col 기준 zero 변환
        for r in range(row_length):
            for z in col_zero:
                matrix[r][z] = 0
