'''
Descrição
Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.

Detalhamento:

Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.

Entrada
Uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano.

Saída
Um único número inteiro representando o total de vendas e um número decimal representando a média mensal de vendas, separados por um espaço.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190	2120, 176.67
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120	780, 65.00
5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60	390, 32.50

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

Codigo Original: 
def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

# -------------------------------------------- ------------------- ---------------------------------
# -------------------------------------------- ------------------- ---------------------------------
# -------------------------------------------- ------------------- ---------------------------------

Resposta:
def analise_vendas(vendas):
    # Calcula o total de vendas e a média mensal
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    
    # Retorna o resultado no formato solicitado
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converte a string de entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Chama a função para obter a entrada e calcular os resultados
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

# -------------------------------------------- ------------------- ---------------------------------
# -------------------------------------------- ------------------- ---------------------------------
# -------------------------------------------- ------------------- ---------------------------------
'''
Explicação:
Função obter_entrada_vendas():

Usa input() para receber a entrada como uma string.
Divide a string usando split(',') para obter uma lista de strings.
Usa map(int, ...) para converter cada elemento da lista para inteiro.
Converte o resultado de map() em uma lista usando list().
Função analise_vendas():

Calcula o total de vendas usando sum().
Calcula a média mensal dividindo o total pelo número de meses (len(vendas)).
Formata a saída para incluir o total de vendas e a média com duas casas decimais (.2f).
Exemplo de execução:

Entrada: 120,150,170,130,200,250,180,220,210,160,140,190
Saida: 2120, 176.67


'''
