def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Não é possível realizar divisão por zero."


def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = soma(num1, num2)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = divisao(num1, num2)
            print("\n****************************")
            print(f"Resultado: {resultado:.2f}")
            print("****************************\n")
        else:
            print("\n*******************************************************")
            print("Opção inválida. Por favor, escolha uma operação válida.")
            print("*******************************************************\n")


calculadora()
