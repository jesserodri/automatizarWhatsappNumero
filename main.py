import re
import webbrowser as wb
import time

#variaveis globais
whats="wa.me/"

#funções
def check_caracter(string):
#docstring
    """
    -> Essa função conta quantos espaços e/ou
    outros caracteres especificados pelos if/elif da função
    """

    count = 0

    for i in string:
        if i == " ":
            count += 1
        elif i == "-":
            count += 1
        elif i == "(":
            count += 1
        elif i == ")":
            count += 1
        elif i == "+":
            count += 1

    return count
def format_number(num):
    """ :param num: numero de telefone ou celular
        :return: url do whatsapp com o numero formatado
    """
    cont_esp = 0
    taman_num = int(len(num)) - check_caracter(num)
    if taman_num == 13 or taman_num == 11 or taman_num == 9:
        new_num = re.sub(r"[^0-9]", "", num)
        url = wb.open_new(f"https://{whats + new_num}")
    else:
        if taman_num == 10 or taman_num == 12 or taman_num == 14:
            msg = print(f"Numero fornecido: {num}\nNumero de telefone fornecido está com 1 numero a mais "
                        f"e está fora do padrão, tente novamente: ")
            return msg
        elif taman_num < 9:
            msg = print(f"Numero de telefone fornecido está abaixo "
                        f"do padrão, tente novamente: ")
            return msg
        elif taman_num > 13:
            msg = print(f"Numero de telefone fornecido está acima "
                        f"do padrão, tente novamente: ")
            return msg

    return url

    time.sleep(3)

#Execução do programa
while True:
    num = input("Forneça o numero para configuração: ").strip()
    format_number(num)






