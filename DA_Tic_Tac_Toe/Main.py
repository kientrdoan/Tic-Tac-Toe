"""
EX8: Game Tic_Tac_Toe
DOAN TRUNG KIEN
N20DCCN027
"""

import pygame
import CheckButton
import Music
from Board import *
from Computer import *


class Game:
    def __init__(self):
        """
        YELLOW: Mau duong thang noi dong hoac cot khi chien thang
        start_x: Toa do vi tri danh cot dau tien
        start_y: Toa do vi tri danh dong dau tien
        squard: Do rong cua moi o game
        """
        self.__YELLOW = (205, 149, 12)
        self.start_x = 32
        self.start_y = 276
        self.squard = 125
        self.board = Board()
        self.computer = Computer()

    #Ve X hoac O the hien nguoi danh
    def draw_turn(self, player):
        if player == 1:
            screen.blit(pygame.image.load(r'Image\first_turn.png'), (100, 35))
        elif player == 2:
            screen.blit(pygame.image.load(r'Image\second_turn.png'), (100, 35))
    
    #Ke Duong Thuong Bao Nguoi Thang
    def draw_line_win(self, row, col, player):
        if self.board.gird[row][0] == player and self.board.gird[row][1] == player and self.board.gird[row][2] == player: #Tren cung mot hang
            pygame.draw.line(screen, self.__YELLOW, (self.start_x - 10, self.start_y + (90)//2+row*(self.squard-18) + row*14), (self.start_x + self.squard*3, self.start_y + (90)//2+row*(self.squard-18) + row*14), 5)
    
        if self.board.gird[0][col] == player and self.board.gird[1][col] == player and self.board.gird[2][col] == player: #Tren cung mot co
            pygame.draw.line(screen, self.__YELLOW, (self.start_x + (100)//2 + col*self.squard + col*10, self.start_y), (self.start_x + (100)//2  + col*self.squard + col*10, self.start_y + (self.squard-15)*3), 5)
    
        if self.board.gird[0][0] == player and self.board.gird[1][1] == player and self.board.gird[2][2] == player:
            pygame.draw.line(screen, self.__YELLOW, (self.start_x + 10, self.start_y + 10), ((self.squard-18)*(3) + self.start_x + 30, self.start_y + (self.squard-18)*(3)), 5)
            
        if self.board.gird[0][2] == player and self.board.gird[1][1] == player and self.board.gird[2][0] == player:
            pygame.draw.line(screen, self.__YELLOW, ((self.squard-18)*(3) + self.start_x + 30, self.start_y + 10), (self.start_x + 10, self.start_y + (self.squard-18)*(3) - 10), 5)

    #Thong Bao Nguoi Chien Thang
    def statement_win_computer(self, player):
        pygame.display.flip()
        start_time = pygame.time.get_ticks()
        last = start_time
        while True:
            start_time = pygame.time.get_ticks()
            if start_time - last >= 1000:
                if player == 'player':
                    screen.blit(pygame.image.load(r'Image\state_win.png'), (0, 251))
                elif player == 'bot':
                    screen.blit(pygame.image.load(r'Image\state_lose.png'), (0, 251))
                else:
                    screen.blit(pygame.image.load(r'Image\state_draw.png'), (0, 251))
                break

    def statement_win_friend(self, player):
        pygame.display.flip()
        start_time = pygame.time.get_ticks()
        last = start_time
        while True:
            start_time = pygame.time.get_ticks()
            if start_time - last >= 1000:
                if player == 1:
                    screen.blit(pygame.image.load(r'Image\x_win.png'), (0, 251))
                elif player == 2:
                    screen.blit(pygame.image.load(r'Image\o_win.png'), (0, 251))
                else:
                    screen.blit(pygame.image.load(r'Image\state_draw.png'), (0, 251))
                break
    
    #Ve Luot Nguoi Danh
    def draw_maker(self, row, col, player): #col x row y
        if player == 1:
            screen.blit(pygame.image.load(r'Image\turnX.png'), (self.start_x + col*(self.squard-1) + col*10, self.start_y + row*(self.squard-18) + row*14))
        if player == 2:
            screen.blit(pygame.image.load(r'Image\turn_o.png'), (self.start_x  + col*(self.squard-1) + col*10, self.start_y + row*(self.squard-18) + row*14))

    #Bieu Tuong Reset Ve Trang Thai Ban Dau
    def draw_button_reset(self):
        screen.blit(pygame.image.load(r'Image\reset.png'), (160, 0))

    #Cap Nhat Bieu Tuong Am Thanh
    def draw_sound(self, play_music):  
        if play_music:
            screen.blit(pygame.image.load(r'Image\sound.png'), (350, 10))
        else:
            screen.blit(pygame.image.load(r'Image\unsound.png'), (350, 10))
    
    #Menu Trang Thai Mo Dau
    def start(self):
        screen.blit(pygame.image.load(r'Image\menugame.png'), (0, 0))

    #Nguoi Choi Chon PlayerX Hoac PlayerO
    def draw_choice_player(self):
        screen.blit(pygame.image.load(r'Image\chose_player.png'), (0, 0))

    #Chon Che Do Danh Easy Hoac Medium
    def draw_choice_mode(self):
        screen.blit(pygame.image.load(r'Image\Mode.png'), (0, 0))

    #Ban Danh Tic_Tac_Toe
    def draw_table(self, player):
        if(player == 1):
            screen.blit(pygame.image.load(r'Image\table.png'), (0,0))
        else:
            screen.blit(pygame.image.load(r'Image\table2.png'), (0,0))



if __name__ == '__main__':
    #Khoi Tao Game
    pygame.init()
    #Tao Cua So Game
    screen = pygame.display.set_mode((435, 650))
    #Tieu De Cua Game
    pygame.display.set_caption("EX8: Game Tic-Tac-Toe")
    #Icon
    pygame.display.set_icon(pygame.image.load(r'Image\icon.png'))

    run_game = True #Xac dinh ket thuc van co
    choice_player = False
    hai_nguoi_danh = False
    may_danh = False
    random_choice = False
    minimax_choice = False
    play_music = True
    next_move = 1

    game = Game()
    computer = game.computer
    board = game.board

    game.start()
    game.draw_sound(play_music)
    Music.load_musci_menu()


    running = True
    #Dung de xet FPS toc do cho game
    clock = pygame.time.Clock()
    while running:
        clock.tick(60) #60 lan trong mot giay

        for event in pygame.event.get(): #Khi nao di chuyen chuot for moi chay
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_x = event.pos[0] # x
                mouse_y = event.pos[1] # y

                #Kiem Tra Nhan Thoat
                if CheckButton.check_exit(mouse_x, mouse_y) and may_danh == False and hai_nguoi_danh == False:
                    running = False

                #Tat Mo Am Thanh
                if CheckButton.check_pause(mouse_x, mouse_y):
                    Music.puase_music_menu(play_music)
                    play_music = not play_music
                    game.draw_sound(play_music)

                #Kiem Tra Thoat Khoi Lua Chon Che Do Danh
                if CheckButton.exit_mode(mouse_x, mouse_y) and may_danh == True and random_choice == False and minimax_choice == False:
                    may_danh = False
                    mouse_x = 0
                    mouse_y = 0
                    game.start()
                    game.draw_sound(play_music)
                    continue
                
                #Kiem Tra Thoat Khoi Che Do Chon Player
                if CheckButton.exit_choice_player(mouse_x, mouse_y) and hai_nguoi_danh == False and may_danh == True and choice_player == False and (minimax_choice == True or random_choice == True):
                    random_choice = False
                    minimax_choice = False
                    mouse_x = 0
                    mouse_y = 0
                    game.draw_choice_mode()
                    game.draw_sound(play_music)
                    continue
                
                #Chon Che Do Hai Nguoi Danh
                if CheckButton.check_play_with_friend(mouse_x, mouse_y) and random_choice == False and minimax_choice == False and may_danh == False and hai_nguoi_danh == False and choice_player == False:
                    computer.player = 1
                    hai_nguoi_danh = True  
                    game.draw_table(computer.player)
                    game.draw_turn(computer.player)
                    game.draw_button_reset()
                    game.draw_sound(play_music)
                    mouse_x = 0
                    mouse_y = 0
                
                #Che Do Danh May Hien Thi Lua Chon
                if CheckButton.check_play_with_computer(mouse_x, mouse_y) and random_choice == False and minimax_choice == False and may_danh == False and hai_nguoi_danh == False and choice_player == False:
                    mouse_x = 0
                    mouse_y = 0
                    may_danh = True
                    game.draw_choice_mode() 
                    game.draw_sound(play_music)                
                
                #Danh Che Do Random
                if CheckButton.check_easy_mode(mouse_x, mouse_y) and random_choice == False and minimax_choice == False and hai_nguoi_danh == False and may_danh == True:
                    game.draw_choice_player()
                    game.draw_sound(play_music)
                    random_choice = True
                    mouse_x = 0
                    mouse_y = 0
                    continue
                
                #Danh Che Do Thuat Toan
                if CheckButton.check_medium_mode(mouse_x, mouse_y) and random_choice == False and minimax_choice == False and hai_nguoi_danh == False and may_danh == True:
                    game.draw_choice_player()
                    game.draw_sound(play_music)
                    minimax_choice = True
                    mouse_x = 0
                    mouse_y = 0
                    continue

                # #Chon Luot Player 1
                if CheckButton.choice_play_first(mouse_x, mouse_y) and may_danh == True and (random_choice == True or minimax_choice == True)and hai_nguoi_danh == False and choice_player == False:
                    mouse_x = 0
                    mouse_y = 0
                    choice_player = True
                    next_move = 1
                    computer.player = 1
                    computer.bot = 2
                    game.draw_table(computer.player)
                    game.draw_sound(play_music)
                    game.draw_button_reset()
                    game.draw_turn(next_move)
                    continue
                
                # #Chon Luot Player 2
                if CheckButton.choice_play_second(mouse_x, mouse_y) and may_danh == True and (random_choice == True or minimax_choice == True) and  hai_nguoi_danh == False and choice_player == False:
                    mouse_x = 0
                    mouse_y = 0
                    next_move = 2
                    computer.bot = 1
                    computer.player = 2
                    game.draw_table(computer.player)
                    game.draw_button_reset()
                    game.draw_turn(computer.bot)
                    game.draw_sound(play_music)
                    choice_player = True
                    continue

                if hai_nguoi_danh:
                    clicked_row = int((mouse_y-game.start_y)//game.squard)
                    clicked_col = int((mouse_x-game.start_x)//game.squard)

                    if game.start_x < mouse_x < game.start_x + game.squard*3 and game.start_y < mouse_y < game.start_y+game.squard*3 and board.is_mark_square(clicked_row, clicked_col) and run_game:
                        
                        board.mark_square(clicked_row, clicked_col, computer.player)
                        game.draw_maker(clicked_row, clicked_col, computer.player)
                        
                        if board.check_win(clicked_row, clicked_col, computer.player):
                            game.draw_line_win(clicked_row, clicked_col, computer.player)
                            game.statement_win_friend(computer.player) 
                            run_game = False

                        computer.player = computer.player%2 + 1
                        game.draw_turn(computer.player)
                        
                        if board.check_gird() and run_game:
                            game.statement_win_friend(0)

                    #reset
                    if CheckButton.check_reset(mouse_x, mouse_y):
                        run_game = True
                        board.gird = board.reset_state()[1]
                        computer.player = 1    
                        game.draw_table(computer.player)
                        game.draw_turn(computer.player)
                        game.draw_button_reset()
                        game.draw_sound(play_music)

                    #exit
                    if CheckButton.exit_play(mouse_x, mouse_y):
                        run_game = True
                        computer.player = 1
                        board.gird = board.reset_state()[1]
                        game.start()
                        game.draw_sound(play_music)
                        hai_nguoi_danh = False

            #May Danh Theo Random
            if random_choice and choice_player:
                if next_move == 1 and run_game:
                    font = pygame.font.SysFont(None, 50)
                    clicked_row = int((mouse_y-game.start_y)//game.squard)
                    clicked_col = int((mouse_x-game.start_x)//game.squard)
                    
                    if game.start_x < mouse_x < game.start_x + game.squard*3 and game.start_y < mouse_y < game.start_y+game.squard*3 and board.is_mark_square(clicked_row, clicked_col) and run_game:                          
                        board.mark_square(clicked_row, clicked_col, computer.player)
                        game.draw_maker(clicked_row, clicked_col, computer.player)
                        if board.check_win(clicked_row, clicked_col, computer.player):
                            game.draw_line_win(clicked_row, clicked_col, computer.player)
                            game.statement_win_computer("player")
                            run_game = False   
                        next_move = next_move % 2 + 1
                        game.draw_turn(computer.bot)
                        

                elif next_move == 2 and run_game:
                    font = pygame.font.SysFont(None, 50)
                    run_game = computer.Random(board, game)
                    next_move = next_move%2 + 1  
                    game.draw_turn(computer.player)              

                if board.check_gird() and run_game:
                    game.statement_win_computer("draw")
                    run_game = False

                #Reset
                if CheckButton.check_reset(mouse_x, mouse_y):
                    game.draw_table(computer.player)
                    game.draw_button_reset()
                    game.draw_turn(1)
                    game.draw_sound(play_music)
                    run_game = True
                    next_move = computer.player
                    mouse_x = 0
                    mouse_y = 0
                    board.choice = board.reset_state()[0]
                    board.gird = board.reset_state()[1]
                    continue

                if CheckButton.exit_play(mouse_x, mouse_y):
                    run_game = True
                    board.choice = board.reset_state()[0]
                    board.gird = board.reset_state()[1]
                    game.draw_choice_player()
                    game.draw_sound(play_music)
                    choice_player = False

            #May Danh Theo Thuat Toan Minimax
            if minimax_choice and choice_player:
                if next_move == 1 and run_game:
                    font = pygame.font.SysFont(None, 50)
                    clicked_row = int((mouse_y-game.start_y)//game.squard)
                    clicked_col = int((mouse_x-game.start_x)//game.squard)

                    if game.start_x < mouse_x < game.start_x + game.squard*3 and game.start_y < mouse_y < game.start_y+game.squard*3 and board.is_mark_square(clicked_row, clicked_col) and run_game:                          
                        board.mark_square(clicked_row, clicked_col, computer.player)
                        game.draw_maker(clicked_row, clicked_col, computer.player)
                        if board.check_win(clicked_row, clicked_col, computer.player):
                            game.statement_win_computer("player")
                            run_game = False 
                         
                        next_move = next_move % 2 + 1
                        game.draw_turn(computer.bot) 

                elif next_move == 2 and run_game:
                    run_game = computer.AI_MOVE(game, board) 
                    next_move = next_move%2 + 1
                    game.draw_turn(computer.player)

                if board.check_gird() and run_game:
                    game.statement_win_computer("draw")
                    run_game = False

                if CheckButton.check_reset(mouse_x, mouse_y):
                    game.draw_table(computer.player)
                    game.draw_button_reset()
                    game.draw_turn(1)
                    game.draw_sound(play_music)
                    run_game = True
                    next_move = computer.player
                    mouse_x = 0
                    mouse_y = 0
                    board.choice = board.reset_state()[0]
                    board.gird = board.reset_state()[1]
                    continue

                if CheckButton.exit_play(mouse_x, mouse_y):
                    run_game = True
                    board.gird = board.reset_state()[1]
                    board.choice = board.reset_state()[0]
                    game.draw_choice_player()
                    game.draw_sound(play_music)
                    choice_player = False
        
        #Cap Nhat Toan Bo Man Hinh Cua So
        pygame.display.flip()
    pygame.quit()


    


