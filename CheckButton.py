import pygame

#Chon Danh Voi May Hoac Hai Nguoi Danh
def check_play_with_computer(xPos, yPos):
    if 60 < xPos < 375 and 440 < yPos < 500:
        return True
    return False

def check_play_with_friend(xPos, yPos):
    if 60 < xPos < 375 and 520 < yPos < 580:
        return True
    return False

def check_exit(xPos, yPos):
    if 20 < xPos < 70 and 20 < yPos < 60:
        return True
    return False


#Che Do EasyBot Hoac MediumBot
def check_easy_mode(xPos, yPos):
    if 165 < xPos < 400 and 205 < yPos < 315:
        return True
    return False

def check_medium_mode(xPos, yPos):
    if 165 < xPos < 400 and 450 < yPos < 560:
        return True
    return False

def exit_mode(xPos, yPos):
    if 40 < xPos < 80 and 20 < yPos < 80:
        return True
    return False

#Chon PlayerX Hoac PlayerO
def choice_play_first(xPos, yPos):
    if 40 < xPos < 360 and 90 < yPos < 290:
        return True
    return False

def choice_play_second(xPos, yPos):
    if 40 < xPos < 360 and 355 < yPos < 555:
        return True
    return False

def exit_choice_player(xPos, yPos):
    if 30 < xPos < 75 and 10 < yPos < 55:
        return True
    return False

#Thoat Khoi Che Do Dang Danh
def exit_play(xPos, yPos):
    if 35 < xPos < 80 and 5 < yPos < 45:
        return True
    return False

#Nut Reset
def check_reset(xPos, yPos):
    if 160 < xPos < 235 and 0 < yPos < 25:
        return True
    return False  

#Pause Music
def check_pause(xPos, yPos):
    if 350 < xPos < 400 and 10 < yPos < 50:
        return True
    return False  



  

