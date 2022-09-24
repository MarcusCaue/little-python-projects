from funcoes import visual
#import pygame

def validação():
    option = str(input("Quer continuar? [S/N] ").upper().strip()[0])
    while option != "S" and option != "N":
        option = str(input("\033[31mValor inválido. Tente novamente: \033[m")).upper().strip()[0]
    return option


def escolha(n=0):
    choice = n
    while choice < 0 or choice > 3:
        visual.escreva("Houve algum erro na sua escolha. Tente novamente: ", 1)
    return choice

"""def toca_música(lst, msc=0):
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(lst[msc - 1])
    pygame.mixer.music.play()
    pygame.event.wait()"""
