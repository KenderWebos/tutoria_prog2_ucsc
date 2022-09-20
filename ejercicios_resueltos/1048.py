#https://www.beecrowd.com.br/judge/es/problems/view/1048

def main():
    salario = float(input())
    if salario <= 400:
        reajuste = salario * 0.15
        novo_salario = salario + reajuste
        percentual = 15
    elif salario <= 800:
        reajuste = salario * 0.12
        novo_salario = salario + reajuste
        percentual = 12
    elif salario <= 1200:
        reajuste = salario * 0.10
        novo_salario = salario + reajuste
        percentual = 10
    elif salario <= 2000:
        reajuste = salario * 0.07
        novo_salario = salario + reajuste
        percentual = 7
    else:
        reajuste = salario * 0.04
        novo_salario = salario + reajuste
        percentual = 4
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: {} %".format(percentual))

    input()

if __name__ == '__main__':
    main()