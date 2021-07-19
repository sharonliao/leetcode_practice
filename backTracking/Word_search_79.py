class Solution(object):
    visited = []
    board = []
    rows = 0
    columns = 0

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        1. 先找起始点
        2. 查找起始点的周围是否可以继续
        3. 定义相邻位置,一般是有四个方向 i,j-1   i, j+1   i-1,j  i+1,j
        3. 注意同一个位置只能用一次，所以要用list存tuple，回退的时候pop
        4. recurisve + backStrack

        A B C E
        S F C S
        A D E E

        ABCCED

        A. B. C. E
        11 12 13 14  ABC
                 C   S
                 23  24   ABCC
                     E
                     33.  ABCCE

        """
        self.rows = len(board)
        print(self.rows)
        self.columns = len(board[0])
        print(self.columns)
        self.board = board

        for r in range(self.rows):
            for c in range(self.columns):
                if board[r][c] == word[0]:
                    self.visited = [(r, c)]
                    if len(word) == 1:
                        return True
                    if self.search((r, c), word[1:]):
                        return True
        return False

    def search(self,position, r_word):
        # i,j-1   i, j+1   i-1,j  i+1,j
        i,j = position
        print(f"{position} {self.board[i][j]} ")
        if len(r_word) == 0:
            return True
        elif len(r_word) > 0:
            if j > 0 and (i, j - 1) not in self.visited and self.board[i][j - 1] == r_word[0]:
                print(2)
                self.visited.append((i, j - 1))
                result = self.search((i, j - 1), r_word[1:])
                if result:
                    return True

            if j + 1 < self.columns and (i, j + 1) not in self.visited and self.board[i][j + 1] == r_word[0]:
                print(3)
                self.visited.append((i, j + 1))
                result = self.search((i, j + 1), r_word[1:])
                if result:
                    return True

            if i > 0 and (i - 1, j) not in self.visited and self.board[i - 1][j] == r_word[0]:
                print(4)
                self.visited.append((i - 1, j))
                result = self.search((i - 1, j), r_word[1:])
                if result:
                    return True

            if i + 1 < self.rows and (i + 1, j) not in self.visited and self.board[i + 1][j] == r_word[0]:
                print(5)
                self.visited.append((i + 1, j))
                result = self.search((i + 1, j), r_word[1:])
                if result:
                    return True
            self.visited.pop()
            return False
        else:
            print(6)
            self.visited.pop()
            return False

# ["A","B","C","E"]
# ["S","F","E","S"]
# ["A","D","E","E"]

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word ="ABCESEEEFS"

test = Solution()
print(test.exist(board,word))




