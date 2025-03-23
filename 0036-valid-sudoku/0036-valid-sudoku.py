class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set=[set() for _ in range(len(board))]
        col_set=[set() for _ in range(len(board))]
        matrix_set=[set() for _ in range(len(board))]

        for r in range(9):
            for c in range(9):

                num=board[r][c]

                #skip if not digit
                if not num.isdigit():
                    continue
                
                #row check
                if num in row_set[r]:
                    print('Condition 1')
                    return False
                else:
                    row_set[r].add(num)
                
                #col check
                if num in col_set[c]:
                    print('Condition 2')
                    return False
                else:
                    col_set[c].add(num)

                #3X3 matrix check
                index=(r//3)*3 + (c//3)
                if num in matrix_set[index]:
                    print('Condition 3')
                    return False
                else:
                    matrix_set[index].add(num)
        return True






        