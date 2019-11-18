cpf = ("529.982.247-25")

def valida_cpf(cpf):
    cpf.replace(".","")
    cpf.replace("-","")
    tam = len(cpf)
    if tam > 11 or tam < 11:
        return False
    elif cpf == "00000000000" or cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999":
        return False
    num_mult = 10
    soma = 0
    for i in range(0, tam-3):
        soma += cpf[i] * num_mult
        num_mult -= 1
        i += 1
    if soma*10//11 == 10:
        if cpf[9] == 0:
            
    
