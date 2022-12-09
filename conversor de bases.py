def conv_para_dec(num_original,base_original):
    num_original = numero
    base_original = int(base_entrada)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x,i in enumerate(dec_temp):
        dec += dic.index(i) * base_original**(x)
    return str(dec)


def dec_para_qualquer(dec,base_final):
    base_final = int(base_saida)
    dec = int(dec)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    numero_final_temp = []
    numero_final = ''
    while True:
        temp_numero_final = dec%base_final
        numero_final_temp.append(temp_numero_final)
        if int(dec/base_final) == 0:
            break
        dec = int(dec/base_final)
    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]     
    return numero_final

def conversor(num_original,base_original,base_final):
    num_dec = conv_para_dec(num_original, base_original)
    num_final = dec_para_qualquer(num_dec, base_final)
    return num_final

base_entrada = input("Digite a base de entrada (2,8,10,16): ")
numero = input("Digite o número que deseja converter: ")
base_saida = input("Digite a base de saída (2,8,10,16): ")

print("O número convertido é: ", conversor(numero,base_entrada,base_saida))