print("Escolha a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if operacao == "1":
    resultado = valor1 + valor2
    print("Resultado: ", resultado)
elif operacao == "2":
    resultado = valor1 - valor2
    print("Resultado: ", resultado)
elif operacao == "3":
    resultado = valor1 * valor2
    print("Resultado: ", resultado)
elif operacao == "4":
    resultado = valor1 / valor2
    print("Resultado: ", resultado)
else:
    print("Operação inválida.")