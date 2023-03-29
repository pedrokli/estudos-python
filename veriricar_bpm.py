#esse programa tem o intuio de verificar se o BPM do usuário está na faixa correta de sua idade

#solicitando as informações do usuário
idade = int(input("Insira o valor da sua idade: "))
bpm = int(input("Insira o seu valor de Batimentos Por Minuto: "))

#checando a condição da idade
if idade >= 8 and idade <= 17:
    if bpm < 80:
        print("O seu batimento está ABAIXO do recomendado para sua idade.")
    elif bpm > 100:
        print("O seu batimento está ACIMA do recomendado para sua idade.")
    else:
        print("O seu batimento está no nível recomendado para sua idade")

elif idade > 17 and idade < 60:
    if bpm < 70:
        print("O seu batimento está ABAIXO do recomendado para sua idade.")
    elif bpm > 80:
        print("O seu batimento está ACIMA do recomendado para sua idade.")
    else:
        print("O seu batimento está no nível recomendado para sua idade")
else:
    if bpm < 50:
        print("O seu batimento está ABAIXO do recomendado para sua idade.")
    elif bpm > 60:
        print("O seu batimento está ACIMA do recomendado para sua idade.")
    else:
        print("O seu batimento está no nível recomendado para sua idade")
