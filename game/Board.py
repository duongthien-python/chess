class board:
    def __init__(self):
        self.grid = [[None]*8 for _ in range(8)]
        self.turn = "white"

    def set_up_piece(self,piece):
        if piece.name=="P":    
            for i in range(8):
                if piece.color=="W":
                    self.grid[1][i]= piece
                else: self.grid[-2][-(i+1)]= piece
        elif piece.name== "R":
            if piece.color=="W":
                self.grid[0][0]= piece
                self.grid[0][-1]= piece
            else: 
                self.grid[-1][0]=piece
                self.grid[-1][-1]= piece
        elif piece.name=="N":
            if piece.color=="W":
                self.grid[0][1]= piece
                self.grid[0][-2]= piece
            else:
                self.grid[-1][1]= piece
                self.grid[-1][-2]= piece
        elif piece.name== "B":
            if piece.color=="W":
                self.grid[0][2]= piece
                self.grid[0][-3]= piece
            else:
                self.grid[-1][2]= piece
                self.grid[-1][-3]= piece
        elif piece.name=="K":
            if piece.color=="W":
                self.grid[0][3]= piece
            else:
                self.grid[-1][3]= piece
        else:
            if piece.color=="W":
                self.grid[0][4]= piece
            else:
                self.grid[-1][4]= piece
    def in_bounds(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def get(self, x, y):
        return self.grid[x][y]

    def get_piece(self, x, y):
        return self.grid[x][y] 

    def promote_pawn(self, x, y, new_piece) :
        self.grid[x][y] = new_piece

    def is_empty(self, x, y):
        return self.get(x, y) is None

    def is_enemy(self, x, y, color):
        p = self.get(x, y)
        return p and p.color != color
