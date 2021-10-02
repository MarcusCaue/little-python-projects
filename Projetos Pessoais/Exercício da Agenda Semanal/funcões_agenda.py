def title(msg):
    print("=" * 50)
    print(f"\033[31m{msg.upper().center(50)}\033[m")
    print("=" * 50)

def verifica_opção(opções):
    print("Opções disponíveis: \n")
    for item in opções:
        print(f"    {opções.index(item) + 1} - {item}")
    
    escolha = int(input("\nDigite aqui o número referente à opção que você deseja: "))
    while escolha > len(opções) or escolha < 1:
        escolha = int(input("Valor inválido. Tente novamente: "))

    return escolha

def gerar_agenda():
    return {'Segunda': {'Matemática': '7:00 - 08:40', 'Química': '08:40 - 10:40', 'Português': '10:40 - 12:20'},
     
    'Terça': {'Filosofia': '7:00 - 08:40', 'Fund INFO/Redes': '08:40 - 10:40', 'Matemática': '10:40 - 12:20',
    'Geografia': '14:40 - 16:40'},
     
    'Quarta': {'Sociologia': '08:40 - 10:40', 'Física': '10:40 - 12:20', 'Ed. Física': '13:00 - 15:30',
    'Sistemas Operacionais': '15:50 - 17:30'},
     
    'Quinta': {'Biologia': '7:00 - 08:40', 'Redes/SO': '08:40 - 10:40', 'Fund INFO/SO': '10:40 - 12:20'},
     
    'Sexta': {'Artes': '7:00 - 08:40', 'Algoritmos': '08:40 - 11:30', 'Português': '11:30 - 12:20'}}

def consulta_horario(dia, agenda):
    dia = dia.strip().title()

    if dia in agenda:
        print(f"Confira as aulas que você terá na \033[32m{dia}\033[m: \n")
        
        for aula, horario in agenda[dia].items():
            print(f"\033[33m{aula}\033[m no intervalo de \033[36m{horario}\033[m")

        print()
    else:
        print("Não foi possível encontrar o dado que você pesquisou.")

def modificar(agenda):
    title('Modificando dados na agenda')

    opção = verifica_opção(['Inserir ou Alterar um dado', 'Remover um dado existente', 'Fechar o sistema'])
    dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    #Fecha o sistema
    if opção == 3:
        title('Fechando a funcionalidade')
        return agenda

    #Inserir/Alterar um dado
    elif opção == 1:
        title('Inserindo/alterando dados')

        dia = input("Insira o nome do dia da semana: ").strip().title()
        while dia not in dias_da_semana:
            dia = input("Valor inválido. Tente novamente: ").strip().title()
        
        matéria = input("Digite o nome da disciplina: ").strip().title()
        horário = input("Insira o valor do horário [Siga o modelo: '00:00']: ").strip()

        if dia not in agenda:
            agenda[dia] = {}

        #Adicionar novos valores
        if matéria not in agenda[dia]:
            agenda[dia].setdefault(matéria, horário)

        #Alterar valores existentes
        else:
            agenda[dia].update({matéria: horário})

        return agenda
    
    #Remover dados
    elif opção == 2:
        title('Removendo dados')
        escolha = verifica_opção(['Excluir toda a agenda', 'Remover todo o conteúdo de um dia', 'Remover uma disciplina'])

        if escolha == 1:
            agenda.clear()
            print("Agenda excluída com sucesso!")
        else:
            dia = input("Insira o nome do dia da semana: ").strip().title()
            while dia not in agenda:
                dia = input("Valor inválido. Tente novamente: ").strip().title()
            
            if escolha == 2:
                del agenda[dia]
            else:
                matéria = input("Digite o nome da disciplina: ").strip().title()
                while matéria not in agenda[dia]:
                    matéria = input("Valor inválido. Tente novamente: ").strip().title()
                
                del agenda[dia][matéria]
            
            return agenda
