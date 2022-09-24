def escreva(msg="", cor="cinza", retorno=True):
    """
    Escreve uma mensagem com cores personalizáveis
    :param msg: Mensagem a ser exibida.
    :param cor: Nome da cor da mensagem
        Obs: Dependendo do tema do editor de código, as cores podem mudar.
    :param retorno: Indica se a função irá retornar a mensagem ou não
    """
    cores = {
        "branco": 0, "vermelho": 1, "amarelo": 2, "verde": 3, "azul": 4, "roxo": 5, "ciano": 6, "cinza": 7
    }

    if retorno:
        return f"\033[3{cores[cor]}m{msg}\033[m"
    else:
        print(f"\033[3{cores[cor]}m{msg}\033[m")


def linha(tamanho, cor="cinza"):
    """
    Mostra uma linha na tela de qualquer tamanho.
    Utiliza a função 'escreva' para colocar cores na linha.
    :param tamanho: Valor numérico que determina o tamanho da linha
    :param cor: Cor da linha. Funciona igual ao da função 'escreva'.
    :return: Nada
    """
    escreva('-=' * tamanho, cor, False)


def título(msg, cor_msg="cinza", cor_linha="cinza"):
    """
    -> Mostra um título formatado e colorido
    com duas linhas separatórias. Tipo um menu
    """
    linha(30, cor_linha)
    escreva(msg.upper().center(50), cor_msg, False)
    linha(30, cor_linha)
