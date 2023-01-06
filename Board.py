class Board:
    def __init__(self):
        """
        gird: Ma tran 3x3 dai dien cho ban co
        choice: Dai dien cho 9 vi tri danh cua ma tran 3x3 gird
        """
        self.gird = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.choice = [(0,0), (0,1), (0,2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    
    #Kiem Tra Xem Nguoi Chien Thang
    def check_win(self, row, col, player):
        #Theo Dong
        if self.gird[row][0] == player and self.gird[row][1] == player and self.gird[row][2] == player:
            return player
        
        #Theo Cot
        if self.gird[0][col] == player and self.gird[1][col] == player and self.gird[2][col] == player:
            return player
        
        #Duong Cheo
        if self.gird[0][0] == player and self.gird[1][1] == player and self.gird[2][2] == player:
            return player
        if self.gird[0][2] == player and self.gird[1][1] == player and self.gird[2][0] == player:
            return player
        return 0
    
    #Kiem Tra Vi Tri Con Trong
    def is_mark_square(self, row, col):
        return self.gird[row][col] == 0

    #Danh Dau Vi Tri Da Danh
    def mark_square(self, row, col, player):
        self.gird[row][col] = player

    #Kiem Tra Da Danh Het Vi Tri Chua Va Kiem Tra Hoa
    def check_gird(self):
        for i in range(len(self.gird)):
            for j in range(len(self.gird[i])):
                if self.gird[i][j] == 0:
                    return False
        return True
    #Tra Ve Trang Thai Ban Dau
    def reset_state(self):
        self.choice = [(0,0), (0,1), (0,2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for i in range(len(self.gird)):
            for j in range(len(self.gird[i])):
                self.gird[i][j] = 0
        return self.choice, self.gird   
