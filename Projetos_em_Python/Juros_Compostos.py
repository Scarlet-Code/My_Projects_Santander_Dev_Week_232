#  Desafio Python: Juros Compostos

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

#  Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
for tempo in range(periodo):
    valor_final = valor_final * (1 + taxa_juros)

print("Valor final do investimento: R$", round (valor_final, 2))

# Exemplo
valor_inicial = float(input(5000))
taxa_juros = float(input(0.08))
periodo = int(input(5))

valor_final = valor_inicial

for tempo in range(periodo):
    valor_final = valor_final * (1 + taxa_juros)

print("Valor final do investimento: R$", round (valor_final, 2))

#  Saída do console
"Valor final do investimento: R$ 7346"
