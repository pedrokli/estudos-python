#solicitando o valor total da compra
valor_da_compra = input("Insira o valor total da sua compra: ")
valor_da_compra = float(valor_da_compra)

#solicitando o cumpo NIVER10
cupom = input("Insira o cupom:")

#condição lógica
if cupom == "NIVER10":
    #descontando os 10%
    valor_final = valor_da_compra * 0.9
else:
    valor_final = valor_da_compra
    print("CUPOM INVÁLIDO")

print("O valor total da compra é R${}".format(valor_final))