#  Desafio Python: O Grande Deposito

valor = float(input())

if valor > 0:
    valor_total = valor
    print('Deposito realizado com sucesso!')  #  Imprimir a mensagem de sucesso e mostra o saldo atual.
    print(f'Saldo atual: R$ {valor_total:.2f}')

elif valor == 0:
   print('Encerrando o programa...')   #  Imprimir a mensagem de encerrar o programa.

else:
  print('Valor inválido! Digite um valor maior que zero.')   #  Imprimir a mensagem de valor inválido.

# Exemplo

valor = float(input(-100))

if valor > 0:
    valor_total = valor
    print('Deposito realizado com sucesso!')  
    print(f'Saldo atual: R$ {valor_total:.2f}')

elif valor == 0:
   print('Encerrando o programa...')  

else:
  print('Valor inválido! Digite um valor maior que zero.') 

#  Saída do Console

"Valor inválido! DIgite um valor maior que zero."