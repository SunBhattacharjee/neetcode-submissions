class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == ".":
                    continue

                if(element in rows[i] or
                    element in cols[j] or
                    element in squares[(i // 3, j // 3)]):
                    return False

                rows[i].add(element)
                cols[j].add(element)
                squares[(i // 3, j // 3)].add(element)

        return True