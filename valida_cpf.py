cpf = ("529.982.247-25")

def valida_cpf(cpf):
    cpf.replace(".","")
    cpf.replace("-","")
    if len(cpf) > 11 or len(cpf) < 11:
        return False
    elif cpf == "00000000000" or cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999":
        return False
    elif 

