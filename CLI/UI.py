class User_interface:
    # def __init__(self):
    #     self.set_up_ui()  # Khởi tạo bàn cờ ở đây
    
    def set_up_ui(self):
        print(" CỜ VUA ".center(40, '='))
        print("1.Chơi online")
        print("2.Chơi 1 mình (alone)")
        print("3.Thoát")
        choice=input("Chọn chế độ chơi: ")
        if choice=='1':
            self.start_online_game()
        elif choice=='2':
            self.start_new_game()
        elif choice=='3':
            print("Thoát game. Hẹn gặp lại!")
    
    def start_online_game():
        pass
    
    # def start_new_game(self):
    #     print("Starting a new game...")
    #     self.show_board()
    @staticmethod
    def show_board(board):
        for i in range(8):
            row = ""
            for j in range(8):
                piece = board.get(i, j)
                if piece is None:
                    row += ". |"
                else:
                    row += piece.name + piece.color + "|"
            print(row+f"  {i+1}")
        print()
        print("a  b  c  d  e  f  g  h")