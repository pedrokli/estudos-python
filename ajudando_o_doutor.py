#solicitando as informações do aluno
email_aluno = input("Insira o e-mail do aluno: ")
nota_aluno = input("Insira a sua nota do semestre: ")
#convertendo a nota para float
nota_aluno = float(nota_aluno)

#condição se a nota for maior que 8.5
if nota_aluno > 8.5:
    print("ENVIANDO CONVITE PARA {}".format(email_aluno))
else:
    print("SUA NOTA ATINGIU A META")