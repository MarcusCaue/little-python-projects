import functions as agenda
from time import sleep

agenda_semanal = {}
agenda_semanal = agenda.gerar_agenda()

while True:
    agenda.title('Agenda semanal')
    opção = agenda.verifica_opção(['Ver a agenda', 'Consultar um horário na agenda', 'Modificar a agenda', 'Fechar o sistema'])

    sleep(1)

    #Fechando o sistema
    if opção == 4:
        agenda.title('Fechando o sistema')
        print("Obrigado e volte sempre! :)")
        break
    
    #Verificando os dados da agenda
    elif opção == 1:
        agenda.title('Verificando os dados da agenda')
        if len(agenda_semanal) == 0:
            print("Agenda vazia!")
        else:
            for valor in agenda_semanal.items():
                
                dia = valor[0]                      #Dias da semana
                disciplina = list(valor[1].keys())  #Disciplinas de cada dia
                aulas = list(valor[1].values())     #Horário das aulas

                print("=" * 150)
                print(f"{dia:<10}", end="")
                for d in disciplina:
                    print(f"\033[33m{d}\033[m -> | \033[36m{aulas[disciplina.index(d)]}\033[m | ", end="")
                print()
    
    #Consultando um horário na agenda
    elif opção == 2:
        agenda.title('Consultando os horários de aula')
        agenda.consulta_horario(input("Digite o dia que você deseja consultar os horários de aula: "), agenda_semanal)

    #Modificando os valores da agenda
    elif opção == 3:
        agenda.modificar(agenda_semanal)
    
    sleep(1)