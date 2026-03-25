nota = float(input("Digite a sua média final: "))
presenca = int(input("Digite a presença em % (0 a 100): "))

if(nota>10 or nota<0):
    print("Nota inválida")
elif(nota>=6 and presenca>=75):
    print("Aprovado")
elif(nota>=4 and presenca>=75):
    print("Exame")
else:
    print("Reprovado")