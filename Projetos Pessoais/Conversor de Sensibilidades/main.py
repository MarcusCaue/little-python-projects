from funcoes import visual, dados

#Menu Inicial
visual.linha(30, 3)
visual.escreva('Conversor de sensibilidade de outros Games para o Valorant', 4)
visual.linha(30, 3)

#Inserção dos primeiros dados
game = str(input(visual.escreva("Insira o jogo que você joga: ", 7, True))).upper().strip()
sens = float(input(visual.escreva("Digite o valor da sua sensibilidade: ", 7, True)))
jogos = [['APEX LEGENDS', 'APEX', 'COUNTER STRIKE', 'CS:GO', 'CS'],
         ['OW', 'OVERWATCH', 'PALADINS DE RICO', 'CALL OF DUTY: WARZONE', 'COD', 'CALL OF DUTY', 'COD: WZ'],
         ['FORTNITE', 'FORTNITRO', 'FORT']]
sensis = [sens / 3.181818, sens / 10.6, sens / 12.6]


option = ""
while option != "N":
    for elemento in range(0, 3):
        if game in jogos[elemento]:
            print("\033[30mA sensibilidade que você deverá colocar no Valorant é de\033[m \033[34m{:.3f}\033[m".format(sensis[elemento]))
    option = str(input("Você deseja inserir outro jogo? ")).strip().upper()[0]
    while option != "N" and option != "S":
        option = str(input("\033[31mValor inválido tente novamente:\033[m ")).strip().upper()[0]
        game = ""
    if option == "S":
        game = str(input("Insira-o: ")).upper().strip()
        sens1 = float(input("Digite novamente a sua sensibilidade: [Digite 0 para usar a atual] "))
        if sens1 == 0:
            sens = sens
        else:
            sens = sens1
            sensis[0] = sens / 3.181818
            sensis[1] = sens / 10.6
            sensis[2] = sens / 12.6
    else:
        print("\033[33m-=\033[m"*11)
        print("\033[35;1mPrograma finalizado!\033[m")
        print("\033[33m-=\033[m"*11)
