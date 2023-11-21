import time
import random

# Função para gerar uma base de dados de teste com números aleatórios
def generate_test_data(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def max_subsequence(arr):
    n = len(arr)
    max_len = 0
    max_subseq = []

    for i in range(2 ** n):
        subseq = [arr[j] for j in range(n) if (i >> j) & 1]
        if all(subseq[k] < subseq[k + 1] for k in range(len(subseq) - 1)):
            if len(subseq) > max_len:
                max_len = len(subseq)
                max_subseq = subseq

    return max_subseq

# Exemplo de uso

test_data_size = 24

# Gerar uma base de dados de teste com números aleatórios entre 1 e 100
test_data = generate_test_data(test_data_size, 1, 100)


def maior_subsequencia_binario(arr):
    n = len(arr)
    # seq_atual[i] armazena a maior subsequência crescente que termina no índice i
    seq_atual = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and seq_atual[i] < seq_atual[j] + 1:
                seq_atual[i] = seq_atual[j] + 1

    # O comprimento da maior subsequência crescente estará no último elemento de seq_atual
    max_comprimento = max(seq_atual)

    # Reconstruir a subsequência
    subsequence = []
    for i in range(n - 1, -1, -1):
        if seq_atual[i] == max_comprimento:
            subsequence.append(arr[i])
            max_comprimento -= 1

    # Inverter a subsequência, pois foi construída de trás para frente
    subsequence.reverse()

    return subsequence

# Exemplo de uso
lista = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("lista:", test_data)
# Medir o tempo de execução para a função maior_subsequencia_binario
result, execution_time = measure_execution_time(maior_subsequencia_binario, test_data)
print("Maior Subsequência Crescente por busca binária:", result)
print("Tempo de execução:", execution_time)

# Medir o tempo de execução para a função max_subsequence
result, execution_time = measure_execution_time(max_subsequence, test_data)
print("Máxima subsequência crescente brute force:", result)
print("Tempo de execução:", execution_time)


'''resultado = maior_subsequencia_binario(lista)
print("Maior Subsequência Crescente por busca binária:", test_data)


resultado = max_subsequence(lista)
print("Máxima subsequência crescente brute force:", test_data)'''
