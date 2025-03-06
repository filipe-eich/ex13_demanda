"""
Programa: demanda
Descrição: Este programa calcula a demanda por um bem com termos à escolha do usuário
Autor: Filipe Eich
Data: 28/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

d=""
r=""
p=""


#Entrada de dados

r=float(input("\nOlá! Vamos calcular a demanda por um bem? Comece me informando a renda do consumidor: R$"))
p=float(input("\nAgora, me informe o preço do bem: R$"))


# Processamento de dados

d=r/p


#Saida de dados

print(f"\nA quantidade demandada pelo consumidor é de {d} unidades!")
