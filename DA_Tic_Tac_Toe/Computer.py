import random

class Computer:
    def __init__(self):
        self.player = 1
        self.bot = 2

    #-------Random-------
    def Random(self, board_obj, game):
        row = 0
        col = 0
        if board_obj.check_gird():
            return False
        while True:
            move = random.randrange(0, len(board_obj.choice), 1)
            row = board_obj.choice[move][0]
            col = board_obj.choice[move][1]
            
            if board_obj.gird[row][col] != 0:
                continue
            else:
                board_obj.gird[row][col] = self.bot
                board_obj.choice.pop(move)
                break 
        game.draw_maker(row, col, self.bot)
        if board_obj.check_win(row, col, self.bot):
            game.draw_line_win(row, col, self.bot)
            game.statement_win_computer("bot")
            return False
        return True

    #-------AI--------
    def AI_MOVE(self, game, board_obj):
        best_score = -100
        best_move = []
        if board_obj.check_gird():
            return False

        for i in range(len(board_obj.gird)):
            for j in range(len(board_obj.gird[i])):
                if(board_obj.is_mark_square(i,j)):
                    board_obj.mark_square(i, j, self.bot)
                    score = self.minimax(board_obj.gird, 0, False, i, j, board_obj)
                    board_obj.gird[i][j] = 0
                    if(score > best_score):
                        best_score = score
                        best_move.append(i)
                        best_move.append(j)
        board_obj.gird[best_move[0]][best_move[1]] = self.bot
        game.draw_maker(best_move[0], best_move[1], self.bot)
        if board_obj.check_win(best_move[0], best_move[1], self.bot):
            game.draw_line_win(best_move[0], best_move[1], self.bot)
            game.statement_win_computer("bot")
            return False
        return True

    def minimax(self, gird, depth, is_maximizing, row, col, board_obj):
    
        if board_obj.check_win(row, col, self.bot):
            return 100
        elif board_obj.check_win(row, col, self.player):
            return -100
        elif board_obj.check_gird():
            return 0
        
        if is_maximizing:
            best_score = -1000

            for i in range(len(board_obj.gird)):
                for j in range(len(board_obj.gird[i])):
                    if(board_obj.is_mark_square(i,j)):
                        board_obj.mark_square(i, j, self.bot)
                        score = self.minimax(board_obj.gird, depth+1, False, i, j, board_obj)
                        board_obj.gird[i][j] = 0
                        if(score > best_score):
                            best_score = score
            return best_score
        else:
            best_score = 800

            for i in range(len(board_obj.gird)):
                for j in range(len(board_obj.gird[i])):
                    if(board_obj.is_mark_square(i,j)):
                        board_obj.mark_square(i, j, self.player)
                        score = self.minimax(board_obj.gird, depth +1, True, i, j, board_obj)
                        board_obj.gird[i][j] = 0
                        if(score < best_score):
                            best_score = score
            return best_score