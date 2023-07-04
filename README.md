# Gerenciamento De Pedidos De ComidaOnline

Este é um código Python que realiza o cálculo do valor total de um conjunto de pedidos com base em um cupom de desconto. Ele solicita ao usuário o número de pedidos, os detalhes de cada pedido e o cupom de desconto. Em seguida, calcula o valor total com o desconto aplicado e exibe o resultado na tela.

O código começa importando o módulo sys.

A função calcular_valor_total_com_desconto(pedidos, cupom) é definida para realizar o cálculo do valor total com base nos pedidos e no cupom de desconto. A função itera sobre os pedidos e calcula a soma dos valores individuais. Em seguida, verifica o tipo de cupom e aplica o desconto correspondente ao valor total. O valor total com desconto é retornado.

A função main() é definida como o ponto de entrada do programa. Ela solicita ao usuário o número de pedidos e, em seguida, itera sobre o número fornecido para capturar os detalhes de cada pedido. Os detalhes do pedido são divididos em nome e valor, convertidos para o formato adequado e adicionados à lista pedidos. Em seguida, é solicitado ao usuário que forneça o cupom de desconto. O valor total com desconto é calculado chamando a função calcular_valor_total_com_desconto() e, por fim, é exibido na tela usando a interpolação de strings.

A instrução if __name__ == "__main__": garante que a função main() seja executada somente se o módulo for executado diretamente (não importado por outro módulo).
