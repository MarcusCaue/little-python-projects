from functions import visual, dados
from time import sleep

while True:
    #Menu Principal
    visual.título('boletim do bimestre e cadastro de alunos', cor_msg="verde")
    print("1 - {}\n2 - {}\n3 - {}\n".format(
        visual.escreva("Cadastrar novo aluno", "azul"), 
        visual.escreva("Ver boletim", "azul"), 
        visual.escreva("Sair do programa", "azul"))
    )

    #Usuário vai escolher uma das funcionalidades para realizar
    option = dados.validação("limite", 3) #Validação da escolha do usuário

    """
    Opção 1: Cadastrar um novo aluno.
    O usuário vai inserir o nome e duas notas do aluno
    Todos os dados serão salvos no arquivo 'dados_alunos.txt'
    """
    if option == 1:
        sleep(1)
        visual.título('cadastro de novo aluno', cor_msg="verde")
        while True:
            dados.cadastro(input("Digite o código dele: "))
            escolha = dados.validação("s/n")
            if escolha == "N":
                visual.escreva("Alunos cadastrados com sucesso!", "amarelo", False)
                break

    #Opção 2: Ver boletim
    #Vai mostrar os dados da lista formatados e com cores
    if option == 2:
        sleep(1)
        visual.título('boletim', cor_msg="verde")
        dados.ver_boletim()

    #Opção 3: Finaliza o programa com uma mensagem de despedida
    if option == 3:
        visual.escreva('Finalizando programa...', "roxo", False)
        sleep(1)
        visual.linha(30)
        visual.escreva("Muito obrigado! Volte sempre! Amo você s2 ^^)", "ciano", False)
        break
