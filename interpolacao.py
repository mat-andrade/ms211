def main():
    pontos = [(2, f(2)), (2.5, f(2.5)), (4, f(4))]
    print(pontos)
    print(lagrange(2, pontos))

def f(x):
    return 1 / x**2

def lagrange(x, pontos):
    n = len(pontos)
    soma = 0
    for k in range(n):
        produto = pontos[k][1]
        for i in range(n):
            if i != k:
                produto *= (x - pontos[i][0])/(pontos[k][0] - pontos[i][0])
        soma += produto
    return soma



if __name__ == "__main__":
    main()