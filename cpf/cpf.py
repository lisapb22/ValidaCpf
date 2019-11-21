def limparString(originalString):
    ''''
    params originalString: uma string de entrada, que pode possuir números ou caracteres especiais
    returns: uma string que contenha apenas os números, sem os caracteres especiais.
    '''
    finalString = ''
    for caracter in originalString:
        if caracter.isdigit():
            finalString += caracter
    return finalString


def verificarTamanho(originalString):
    '''
    params originalString: Uma string que deve ser um CPF
    returns: True se a originalString possui 11 dígitos (considerando apenas números).
    '''
    stringLimpa = limparString(originalString)
    return len(stringLimpa) == 11