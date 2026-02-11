# ============================================
# PROGRAMAÇÃO PARA ECONOMISTAS
# Aula 2: Setup e Python Básico
# Prof. Alexandre Rabelo
# Universidade Presbiteriana Mackenzie - CCSA
# ============================================

"""
OBJETIVOS DA AULA:
1. Entender o conceito de variáveis
2. Conhecer os tipos de dados básicos (int, float, str, bool)
3. Realizar operações aritméticas
4. Usar a função print() para exibir resultados
5. Trabalhar com f-strings para formatação
"""

# ============================================
# PARTE 1: VARIÁVEIS E ATRIBUIÇÃO
# ============================================

# O que é uma variável?
# Uma variável é como uma "caixinha" que guarda um valor
# Damos um NOME para a caixinha e colocamos um VALOR dentro

# Exemplo: Dados econômicos do Brasil
pib_brasil = 2.1        # PIB em trilhões de USD
populacao = 215         # População em milhões
moeda = "Real"          # Moeda oficial

# Para ver o conteúdo de uma variável, usamos print()
print(pib_brasil)
print(populacao)
print(moeda)

# Podemos criar quantas variáveis quisermos!
taxa_desemprego = 7.8
taxa_juros = 10.75
inflacao_anual = 4.62

print(taxa_desemprego)
print(taxa_juros)
print(inflacao_anual)

# ============================================
# PARTE 2: TIPOS DE DADOS
# ============================================

# Python tem vários tipos de dados. Os 4 principais são:

# 1. INTEIROS (int) - números sem vírgula
ano = 2026
numero_estados = 27
habitantes_sp = 46_649_132  # Podemos usar _ para facilitar leitura!

print(ano)
print(numero_estados)
print(habitantes_sp)

# 2. DECIMAIS (float) - números com vírgula (usam PONTO, não vírgula!)
pib_per_capita = 9767.44
temperatura = 23.5
pi = 3.14159

print(pib_per_capita)
print(temperatura)
print(pi)

# ATENÇÃO: Python usa PONTO, não vírgula!
# Correto: 10.75
# Errado: 10,75

# 3. TEXTO (str = string) - entre aspas simples ' ' ou duplas " "
pais = "Brasil"
capital = 'Brasília'
presidente = "Luiz Inácio Lula da Silva"
sigla = 'BR'

print(pais)
print(capital)
print(presidente)
print(sigla)

# 4. BOOLEANOS (bool) - True (verdadeiro) ou False (falso)
# ATENÇÃO: Primeira letra maiúscula!
aprovado = True
reprovado = False
economia_crescendo = True
inflacao_controlada = False

print(aprovado)
print(economia_crescendo)

# Como verificar o tipo de uma variável? Use type()
print(type(ano))                # <class 'int'>
print(type(pib_per_capita))     # <class 'float'>
print(type(pais))               # <class 'str'>
print(type(aprovado))           # <class 'bool'>

# ============================================
# PARTE 3: OPERAÇÕES ARITMÉTICAS
# ============================================

# Python funciona como uma calculadora!

# Adição
resultado1 = 10 + 5
print(resultado1)  # 15

# Subtração
resultado2 = 10 - 5
print(resultado2)  # 5

# Multiplicação
resultado3 = 10 * 5
print(resultado3)  # 50

# Divisão (sempre retorna float!)
resultado4 = 10 / 5
print(resultado4)  # 2.0 (não 2!)

# Potência (** não ^!)
resultado5 = 10 ** 2
print(resultado5)  # 100

# Podemos combinar operações
# Python respeita ordem: () → ** → * / → + -
resultado6 = 2 + 3 * 4
print(resultado6)  # 14 (não 20!)

resultado7 = (2 + 3) * 4
print(resultado7)  # 20

# ============================================
# PARTE 4: OPERAÇÕES COM VARIÁVEIS
# ============================================

# Podemos usar variáveis em cálculos!

# Exemplo 1: Calcular PIB total
pib_trilhoes = 2.1
pib_bilhoes = pib_trilhoes * 1000
print(pib_bilhoes)  # 2100.0

# Exemplo 2: Calcular PIB per capita
# Dados
pib_tri = 2.1           # PIB em trilhões USD
pop_mi = 215            # População em milhões

# Converter para mesma unidade (bilhões)
pib_bi = pib_tri * 1000      # trilhões → bilhões
pop_bi = pop_mi / 1000       # milhões → bilhões

# Calcular PIB per capita
pib_per_capita = pib_bi / pop_bi
print(pib_per_capita)  # 9.767... mil USD per capita

# Exemplo 3: Crescimento econômico
pib_2023 = 2050  # bilhões USD
pib_2024 = 2100  # bilhões USD

crescimento_absoluto = pib_2024 - pib_2023
crescimento_percentual = (crescimento_absoluto / pib_2023) * 100

print(crescimento_absoluto)     # 50 bilhões
print(crescimento_percentual)   # 2.43% aprox

# ============================================
# PARTE 5: FUNÇÃO print() e F-STRINGS
# ============================================

# print() básico: exibe valores
numero = 42
print(numero)

# Mas geralmente queremos texto + valor
# Solução: F-STRINGS!

# Sintaxe: f"texto {variavel}"
# O 'f' antes das aspas ativa a formatação
# As chaves {} são substituídas pelo valor da variável

pib = 2.1
print(f"O PIB do Brasil é ${pib} trilhões")

populacao = 215
print(f"A população é de {populacao} milhões de habitantes")

# Podemos usar múltiplas variáveis!
pais = "Brasil"
capital = "Brasília"
print(f"A capital do {pais} é {capital}")

# F-strings com formatação de casas decimais
taxa = 10.759823
print(f"Taxa de juros: {taxa:.2f}%")  # 10.76%

valor_grande = 1234567.89
print(f"Valor: R$ {valor_grande:,.2f}")  # R$ 1,234,567.89

# ============================================
# PARTE 6: EXEMPLO COMPLETO - ANÁLISE ECONÔMICA
# ============================================


# Dados
pib_trilhoes = 2.1
populacao_milhoes = 215
taxa_desemprego = 7.8
inflacao = 4.62
taxa_juros_selic = 10.75

# Cálculos
pib_bilhoes = pib_trilhoes * 1000
pib_per_capita = (pib_trilhoes * 1000) / (populacao_milhoes / 1000)

# Relatório

print("=" * 50)
print("ANÁLISE ECONÔMICA - BRASIL 2024")
print("=" * 50)
print()
print(f"PIB Total: ${pib_trilhoes:.1f} trilhões (${pib_bilhoes:.0f} bilhões)")
print(f"População: {populacao_milhoes} milhões de habitantes")
print(f"PIB per capita: ${pib_per_capita:,.2f} mil")
print()
print("Indicadores:")
print(f"  • Taxa de desemprego: {taxa_desemprego}%")
print(f"  • Inflação anual (IPCA): {inflacao}%")
print(f"  • Taxa Selic: {taxa_juros_selic}%")
print()
print(f"Conclusão: Inflação {'controlada' if inflacao < 5 else 'elevada'} em 2024.")

# Análise simples (outra forma)
if inflacao < 5:
    situacao_inflacao = "controlada"
else:
    situacao_inflacao = "elevada"

print(f"\nConclusão: Inflação {situacao_inflacao} em 2024.")

# ============================================
# EXERCÍCIOS PARA PRATICAR
# ============================================

print("="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1: Crie variáveis para outro país e identifique o tipo de cada variável
# - PIB (trilhões USD)
# - População (milhões)
# - Moeda
# - Taxa de inflação
# - Ano atual
# - Faz parte do mercosul: True

# Seu código aqui:


# EXERCÍCIO 2: Calcule o PIB per capita desse país.
# Dica: Converta as unidades para que façam sentido!

# Seu código aqui:


# EXERCÍCIO 3: Compare com o Brasil
#Use f-strings para criar mensagens formatadas do tipo:
#1. "O PIB per capita do Brasil é X mil USD, enquanto o PIB do País escolhido é Y" (Valores com 2 casas decimais).
#2. "A população brasileira é de Y milhões de habitantes, enquanto a população do pais escolhido é de Z milhões de habitantes" (sem decimais, mas com separador de milhar.)

# Seu código aqui:


# EXERCÍCIO 4: Crie um relatório comparando **Brasil** e **Argentina**:
#**Dados:**
#- Brasil: PIB = 2.1 tri, Pop = 215 mi
#- Argentina: PIB = 0.63 tri, Pop = 46 mi
#**Calcule:**
#1. PIB per capita de cada país
#2. Diferença percentual de PIB per capita
#3. Exiba tudo formatado!

# Seu código aqui:

# EXERCÍCIO 5: Conversão de moedas
#Dado que **1 USD = 5.20 BRL** e o salário de um indivíduo é de 5 mil reais, calcule quanto é o salário deste indivíduo em dólares.
#Exiba o salário formatado em duas casas decimais e com separador de milhar.
# Seu código aqui:


# EXERCÍCIO 6: Crescimento populacional
#Considere os seguintes dados:
#- População 2020: 221.8 milhões
#- População 2024: 215.0 milhões
# Calcule:
# a) Crescimento absoluto
# b) Crescimento percentual
# c) Exiba com f-strings formatadas
# Seu código aqui:


# ============================================
# DESAFIO EXTRA 
# ============================================

# Crie um mini-relatório de comparação econômica entre 3 países:
# - Brasil, Argentina e Chile
# - Para cada um: PIB, População, PIB per capita
# - Use f-strings para formatar o mini relatório
# - Calcule qual país tem o maior PIB per capita
# Seu código aqui:



# ============================================
# RESUMO DA AULA
# ============================================

print("="*50)
print("RESUMO - O QUE APRENDEMOS HOJE")
print("="*50)

print("""
1. VARIÁVEIS: "caixinhas" que guardam valores
   - Sintaxe: nome = valor
   - Use nomes descritivos!

2. TIPOS DE DADOS:
   - int: números inteiros (ano = 2026)
   - float: números decimais (taxa = 10.75)
   - str: texto entre aspas (pais = "Brasil")
   - bool: True ou False (aprovado = True)

3. OPERAÇÕES:
   - Aritméticas: + - * / **
   - Ordem: () → ** → * / → + -

4. PRINT() e F-STRINGS:
   - print(variavel) - exibe valor
   - f"texto {variavel}" - combina texto e valor
   - f"{variavel:.2f}" - formata com 2 casas decimais

5. BOAS PRÁTICAS:
   - Comentários explicam o código
   - Nomes de variáveis descritivos
   - Use _ em números grandes (1_000_000)
   - Python usa PONTO para decimais, não vírgula!
""")

# ============================================
# PARA CASA
# ============================================


print("""
1. LEITURA:
   - McKinney, Cap. 2 (p. 17-41): Python Language Basics
   - Coding for Economists, Cap. 2.1-2.3: Basics

2. PRÁTICA:
   - Completar os exercícios acima.
   - Experimentar com dados de outros países.

3. PRÓXIMA AULA:
   - Listas e Dicionários.
   - Como guardar VÁRIOS dados ao mesmo tempo.
   - Estruturas fundamentais para análise de dados.

""")

print("Bons estudos!")

# ============================================
# FIM DO ARQUIVO
# ============================================
