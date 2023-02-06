Binario = int(input('numero binario:'))

n = len(str(Binario))

valor_digitado = Binario
decimal = 0
i = 0

while n >= 0:
    resto = Binario % 10
    decimal = decimal + (resto *(2**i))
    n = n - 1
    i = i + 1
    Binario = Binario // 10

print ('o numero binario digitado ',valor_digitado,' , na base decimal, vale: ', decimal)
