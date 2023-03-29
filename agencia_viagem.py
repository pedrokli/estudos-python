#Esse programa tem o intuito de calcular o desconto progressivo de uma simulação de um pacote de viagem

#Solicitando as informações para a pessoa calcular o pacote
valor_bruto = float(input("Insira o valor bruto do pacote de viagem: "))
categoria = input("Insira o nome da categoria do pacote (Economica, executiva ou primeira classe): ")
numero_pessoas = int(input("Insira no número de pessoas no pacote (Lembrando que o desconto só é válido se as pessoas morarem na mesma casa): "))

#condição da classe economica
if categoria.upper() == "ECONOMICA":
    if numero_pessoas == 2:
        #3% de desconto
        valor_final = valor_bruto * 0.97
    elif numero_pessoas == 3:
        #4% de desconto
        valor_final = valor_bruto * 0.96
    elif numero_pessoas >= 4:
        #5% de desconto
        valor_final = valor_bruto * 0.95
    else:
        print("Por favor, insira um valor válido e tente novamente")

#condição da classe executiva
if categoria.upper() == "EXECUTIVA":
    if numero_pessoas == 2:
        #5% de desconto
        valor_final = valor_bruto * 0.95
    elif numero_pessoas == 3:
        #7% de desconto
        valor_final = valor_bruto * 0.93
    elif numero_pessoas >= 4:
        #8% de desconto
        valor_final = valor_bruto * 0.92
    else:
        print("Por favor, insira um valor válido e tente novamente")

#condição da primeira classe
if categoria.upper() == "PRIMEIRA CLASSE":
    if numero_pessoas == 2:
        #10% de desconto
        valor_final = valor_bruto * 0.9
    elif numero_pessoas == 3:
        #15% de desconto
        valor_final = valor_bruto * 0.85
    elif numero_pessoas >= 4:
        #20% de desconto
        valor_final = valor_bruto * 0.80
    else:
        print("Por favor, insira um valor válido e tente novamente")

#calculo do valor médio por pessoa
valor_medio = valor_final/numero_pessoas

#mostrando o resultado para o usuário
print("Valor Bruto: {}".format(valor_bruto))
print("Valor Líquido: {}".format(valor_final))
print("Valor médio por pessoa do pacote: {}".format(valor_medio))
