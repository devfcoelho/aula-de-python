peso = float(input("Digite o seu peso: (KG) "))
altura = float(input("Digite a sua altura: (cm) "))

imc = peso/ (altura*altura)

print("Seu IMC é: ",imc)
if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<25:
    print("Normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<35:
    print("Obesidade grau I")
else:
    print("Obesidade severa")
