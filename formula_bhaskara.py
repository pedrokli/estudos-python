import math
#esse programa tem o intuito de resolver a fórmula de Bhaskara
a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

#calculo do delta
delta = b * b - 4 * a * c


if delta > 0.0:
    #cálculo de 2 valores para o x
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores x1 = {} e x2 = {}".format(a,b,c,x1,x2))
elif delta == 0.0:
    #cálculo de 1 valor para o x
    x = (-b + math.sqrt(delta)) / 2 * a
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor x = {}".format(a,b,c,x))
else:
    #exibição da mensagem
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a,b,c))

