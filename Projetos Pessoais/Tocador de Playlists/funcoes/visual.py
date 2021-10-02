def escreva(msg="", cor=0):
    """
    Escreve uma mensagem com cores personalizáveis
    :param msg: Mensagem a ser exibida.
    :param cor: Cor da mensagem, que é um valor númerico entre 0 e 7
    :param more: Caso tenha o uso de mais uma cor, a mensagem terá uma alteração
    :return: Nada.
    """
    print(f"\033[3{cor}m{msg}\033[m")


def linha(tamanho, cor=0):
    """
    Mostra uma linha na tela de qualquer tamanho.
    Utiliza a função 'escreva' para colocar cores na linha.
    :param tamanho: Valor numérico que determina o tamanho da linha
    :param cor: Cor da linha. Funciona igual ao da função 'escreva'.
    :return: Nada
    """
    escreva('-=' * tamanho, cor)


def título(msg, cor_msg=0, cor_linha=0):
    """
    -> Mostra um título formatado e colorido
    com duas linhas separatórias. Tipo um menu
    """
    linha(30, cor_linha)
    escreva(msg.upper().center(50), cor_msg)
    linha(30, cor_linha)
