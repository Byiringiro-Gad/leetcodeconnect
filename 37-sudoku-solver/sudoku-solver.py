class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_space = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_index = (r//3)*3 + (c//3)
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_index].add((val))
                else:
                    empty_space.append((r,c))
        
        def soduko(idx):
            if idx >= len(empty_space):
                return True
            
            r, c = empty_space[idx]
            box_index = (r//3)*3 + (c//3)

            for i in "123456789":
                if i not in rows[r] and i not in cols[c] and i not in boxes[box_index]:
                    board[r][c] = i
                    rows[r].add(i)
                    cols[c].add(i)
                    boxes[box_index].add(i)

                    if soduko(idx + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    boxes[box_index].remove(i)
            return False

        soduko(0)