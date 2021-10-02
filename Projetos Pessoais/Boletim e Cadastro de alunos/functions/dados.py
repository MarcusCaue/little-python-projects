from functions.visual import *

def validação(tipo, limite=0):
    
    if tipo == "s/n":
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        while option not in "SN":
            option = input(escreva("Valor inválido. Tente novamente: ", 1, True)).strip().upper()[0]
    
    elif tipo == "limite":
        option = int(input("Digite a sua opção: "))
        while option < 1 or option > limite:
            option = int(input(escreva("Houve algum erro. Tente novamente: ", 1, True)))
    
    return option


def cadastro(code):
    with open("dados_alunos.txt", "a") as arq:
        nome = input("Digite o nome do aluno: ")
        n1 = float(input("Insira 1º nota: "))
        n2 = float(input("Insira 2º nota: "))
        media = str((n1 + n2) / 2)
        n1, n2 = str(n1), str(n2)

        arq.write(f"\nCódigo do Aluno: {code}\nNome do Aluno: {nome}\nNotas do Aluno: {n1}|{n2}\nMédia do Aluno: {media}\n")


def ver_boletim():
    with open("dados_alunos.txt", "r") as arq:
        
        #Vai ler todos os dados contidos no arquivo 'dados_alunos.txt', inserindo-os numa lista
        dados = arq.readlines()

        if len(dados) == 0:
            escreva("Você ainda não inseriu nenhum dado. Tente novamente mais tarde :/", 1)
        else:
            for hollow_space in range(0, dados.count("\n")):
                dados.remove("\n")
            for d in dados:
                dados[dados.index(d)] = d.split()
            
            for d in dados:
                dados[dados.index(d)] = d[-1]

            dados_provisorio = dados.copy()
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

