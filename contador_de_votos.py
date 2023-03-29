#Esse programa tem o intuito de contar os votos de 5 membros de uma empresa e mostrar qual foi o mais selecionado

#solicitando o voto dos membros da empresa
membro_1 = input("Membro 1 => insira o o prêmio desejado (Playstation, Xbox ou Nintendo): ")
membro_2 = input("Membro 2 => insira o o prêmio desejado (Playstation, Xbox ou Nintendo): ")
membro_3 = input("Membro 3 => insira o o prêmio desejado (Playstation, Xbox ou Nintendo): ")
membro_4 = input("Membro 4 => insira o o prêmio desejado (Playstation, Xbox ou Nintendo): ")
membro_5 = input("Membro 5 => insira o o prêmio desejado (Playstation, Xbox ou Nintendo): ")

#criação de um contador para cada voto escolhido
contador_play = 0
contador_xbox = 0
contador_nint = 0

#lógica para contar o voto por cada membro
if membro_1.upper() == "PLAYSTATION":
    contador_play += 1
elif membro_1.upper() == "XBOX":
    contador_xbox += 1
elif membro_1.upper() == "NINTENDO":
    contador_nint += 1
else:
    print("Como digitou um valor inválido, o voto será desconsiderado")

if membro_2.upper() == "PLAYSTATION":
    contador_play += 1
elif membro_2.upper() == "XBOX":
    contador_xbox += 1
elif membro_2.upper() == "NINTENDO":
    contador_nint += 1
else:
    print("Como digitou um valor inválido, o voto será desconsiderado")

if membro_3.upper() == "PLAYSTATION":
    contador_play += 1
elif membro_3.upper() == "XBOX":
    contador_xbox += 1
elif membro_3.upper() == "NINTENDO":
    contador_nint += 1
else:
    print("Como digitou um valor inválido, o voto será desconsiderado")

if membro_4.upper() == "PLAYSTATION":
    contador_play += 1
elif membro_4.upper() == "XBOX":
    contador_xbox += 1
elif membro_4.upper() == "NINTENDO":
    contador_nint += 1
else:
    print("Como digitou um valor inválido, o voto será desconsiderado")

if membro_5.upper() == "PLAYSTATION":
    contador_play += 1
elif membro_5.upper() == "XBOX":
    contador_xbox += 1
elif membro_5.upper() == "NINTENDO":
    contador_nint += 1
else:
    print("Como digitou um valor inválido, o voto será desconsiderado")

#Comando para mostrar o número de votos que houveram em cada prêmio
print("Playstation: {}\nXbox: {}\nNintendo: {}".format(contador_play,contador_xbox, contador_nint))

#lógica para encontra o mais votado
if contador_play > contador_xbox and contador_play > contador_nint:
    print("O prêmio escolhido é um PLAYSTATION!")
elif contador_xbox > contador_play and contador_xbox > contador_nint:
    print("O prêmio escolhido é um XBOX!")
elif contador_nint > contador_play and contador_nint > contador_xbox:
    print("O prêmio escolhido é um NINTENDO!")
else:
    print("Houve um empate, por favor, entrar em contato com a diretoria.")