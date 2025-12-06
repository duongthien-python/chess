from game.Board import board
from game.chess_pieces import *
from CLI.UI import User_interface


board_game= board()
ui= User_interface()

def making_board():
    pieces= { 
        "pawn":[Pawn("W"),Pawn("b")],
        "King":[King("W"),King("b")],
        "Queen": [Queen("W"),Queen("b")],
        "Rook": [Rook("W"),Rook("b")],
        "Kni": [Knight("W"), Knight("b")],
        "Bishop": [Bishop("W"), Bishop("b")] 
    }
    for i in pieces:
        board_game.set_up_piece(pieces[i][0])
        board_game.set_up_piece(pieces[i][1])
    return board_game

board_game=making_board()
ui.show_board(board_game)
end= False
while not end:
    # đây sẽ là luồng chính nếu em muốn test module
    # giả sử như di chuyển hay check luật em cứ nhét vào đây
    pass