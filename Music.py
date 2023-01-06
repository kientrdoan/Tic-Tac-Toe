import pygame

def load_musci_menu():
    menu_mucsic = pygame.mixer.Sound(r'Music\music.wav')
    menu_mucsic.play(loops=-1)

def puase_music_menu(play_music):
    if play_music:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()
