#  Desafio Python: Equilibrando Saldo

saldo_atual = float(int())
valor_deposito = float(int())
valor_retirada = float(int())

#  Calcular o saldo  atualizado de acordo com a descrição deste desafio.

saldo_atualizado = float(saldo_atual + valor_deposito - valor_retirada)
#  Imprimir a saída conforme a tabela de exemplos (uma casa decimal)

print(f'Saldo atualizado na conta: {saldo_atualizado:.1f}')

#  Exemplo de cálculo

saldo_atual = float(int(1000))
valor_deposito = float(int(500))
valor_retirada = float(int(200))

saldo_atualizado = float(saldo_atual + valor_deposito - valor_retirada)

print(f'Saldo atualizado na conta: {saldo_atualizado:.1f}')

#  Saída no console
'''Saldo atualizado na conta: 1300.0'''

