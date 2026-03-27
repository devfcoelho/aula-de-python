dias_trablhados = int(input("Quantos dias foram trabalhados? "))
valor_diária =  150

Valor_total = dias_trablhados * valor_diária
descontos = Valor_total * 0.22

Valor_Final = Valor_total - descontos
print("O total a ser pago já com os descontos é de: ", Valor_Final)
