class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def postion(pos):
          row = (pos -1)//n 
          col = (pos -1)%n 
          if row%2:
            col = n - 1 - col 
          return [row,col]
        
        queue = deque()
        queue.append([1,0])
        visited = set()
        while queue:
          pos , moves = queue.popleft()
          for i in range(1,7):
            nextpos = pos + i 
            row,col = postion(nextpos)
            if board[row][col] != -1:
              nextpos = board[row][col]
            if nextpos == n*n:
              return moves+1
            if nextpos not in visited:
              queue.append((nextpos,moves+1))
              visited.add(nextpos)
        return -1