from functions.visual import *


with open("dados_alunos.txt", "r") as arq:
    #Vai ler todos os dados contidos no arquivo 'dados_alunos.txt', inserindo-os numa lista
    dados = arq.readlines()

    if len(dados) == 0:
        escreva("Você ainda não inseriu nenhum dado. Tente novamente mais tarde :/", 1)
    else:

        #Vai remover as quebras de linha ("linhas vazias") entre os conjuntos de dados de cada aluno no arquivo
        quebrasDeLinha = 0
        while quebrasDeLinha < dados.count("\n"):
            dados.remove("\n")

        #Cada linha do arquivo será transformado em uma lista onde cada elemento é uma palavra do arquivo
        for linha in dados:
            dados[dados.index(linha)] = linha.split()
        
        #Os dados são os últimos elementos das listas que foram criadas anteriormente. Dessa 
        for dadoAluno in dados:
            dados[dados.index(dadoAluno)] = dadoAluno[-1]
        

        """dados_provisorio = dados.copy()
        dados.clear()
        for pos in range(0, int(len(dados_provisorio)), 4):
            dados.append([dados_provisorio[pos], dados_provisorio[pos + 1], dados_provisorio[pos + 2], dados_provisorio[pos + 3]])
        del dados_provisorio
    
        for notas in range(0, len(dados)):
            dados[notas][2] = dados[notas][2].split("|")

        escreva(f"{'Código':<10} {'Nome':^28} {'Média':>20}", 2)
        for aluno in range(0, len(dados)):
            escreva(f"{dados[aluno][0]:<10} {dados[aluno][1]:^28} {dados[aluno][3]:>20}")

        while True:
            linha(30)

            code = int(input("Insira o código do aluno para ver as suas notas [Digite 999 para interromper]: "))
            
            while (code < 0) or (code >= len(dados) and code != 999):
                code = int(input("\033[31mValor inválido. Tente novamente: \033[m"))
            if code == 999:
                escreva("Voltando para o menu...", 5)
                break

            print("O aluno de nome {} possui as seguintes notas: {}".format(
                escreva(f'{dados[code][1]}', 2, True),
                escreva(f'{dados[code][2]}', 6, True)))
    """
