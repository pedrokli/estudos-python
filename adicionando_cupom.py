#solicitando o valor total da compra
valor_da_compra = input("Insira o valor total da sua compra: ")
valor_da_compra = float(valor_da_compra)

#solicitando o cumpo NIVER10
cupom = input("Insira o cupom:")

#caso o cupom esteja correto, realizará um desconto de 10%
if cupom == "NIVER10":
    valor_da_compra = valor_da_compra * 0.9
    print("O valor da compra com desconto é R${}".format(valor_da_compra))
else:
    print("Como o cupom é inválido, o valor da compra é R${}".format(valor_da_compra))