import sys

def calcular_valor_total_com_desconto(pedidos, cupom):
    valor_total = sum(pedido[1] for pedido in pedidos)
    if cupom == '10%':
        valor_total *= 0.9
    elif cupom == '20%':
        valor_total *= 0.8
    return valor_total

def main():
    n = int(input())

    pedidos = []

    for _ in range(n):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        pedidos.append((nome, valor))

    cupom = input().strip()

    valor_total_com_desconto = calcular_valor_total_com_desconto(pedidos, cupom)

    print(f"Valor total: {valor_total_com_desconto:.2f}")

if __name__ == "__main__":
    main()
