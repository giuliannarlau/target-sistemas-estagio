def check_fibonacci(num):
    """ Verifica se a variável passada como parâmetro faz parte da sequência Fibonacci.

    A função utiliza um loop para gerar os números da sequência Fibonacci até que o último número gerado
    seja maior ou igual ao número fornecido. Durante cada iteração do loop, a variável 'b' é atribuída à
    soma dos dois valores anteriores. No final, o código verifica se o número fornecido é igual ao último
    número gerado na sequência Fibonacci, retornando True em caso positivo e False em caso negativo.
    """

    if num == 0:
        return True
    
    a, b = 0, 1

    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

if __name__ == "__main__":

    try:
        num = int(input("Informe um número: "))
    except:
        print("Informe um número inteiro válido.")
        exit()

    if check_fibonacci(num):
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")
