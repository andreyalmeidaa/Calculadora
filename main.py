class utilCalc:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Erro: Divisão por zerooooooooooo"
        else:
            return a / b


class calcMenu():
    print("=====================================================")
    print(" ")
    pergunta_01 = int(input("Digite o primeiro valor: "))
    print(" ")
    pergunta_02 = int(input("Digite o segundo valor: "))
    print(" ")
    print("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão")
    print(" ")
    print("=====================================================")
    pergunta_03 = input("Digite o numero da operaçao: ")
    calculadora = utilCalc()

    escolha = {
        "1": calculadora.soma,
        "2": calculadora.subtracao,
        "3": calculadora.multiplicacao,
        "4": calculadora.divisao,
    }

    if pergunta_03 in escolha:
        reultado = escolha[pergunta_03](pergunta_01, pergunta_02)
        if pergunta_03 == "4":
            print(
                f"O seu resultado é: {reultado} e o resto da divisão é: {reultado % 2}"
            )
        else:
            print(f"O seu resultado é: {reultado}")
