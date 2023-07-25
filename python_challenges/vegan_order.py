numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    # TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
    if ehVegano == 's':
      print(f"Pedido {i}: {prato} (Vegano) - {calorias} calorias")
      
    elif ehVegano == 'n':
      print(f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias")