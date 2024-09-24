class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self, venda):
        self.vendas.append(venda)
    
    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.valor
        return total

def main():
    categorias = []
    for i in range(2):
        nome_categoria = input().strip() 
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input().strip()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # TODOS: Exibir o total de vendas usando o método total_vendas:
        print(f'Vendas em {categoria.nome}: {categoria.total_vendas():.1f}')

if __name__ == "__main__":
    main()
    

entrada = {
        "Eletrônicos": [("Celular", 5, 1000),("Fone de Ouvido", 10, 500)],
        "Móveis": [("Mesa", 2, 800),("Cadeira", 4, 400)],
        "Alimentos": [("Arroz", 10, 200),("Feijão", 7, 140)],
        "Jardinagem": [("Planta", 2, 60),("Ferramentas", 1, 100)],
        "Livros": [("Aventuras no Tempo", 1, 80),("Mistérios do Oceano", 2, 90)],
        "Esportes": [("Tênis", 7, 210),("Bola", 3, 120)]
}

saida = {
        "Vendas em Eletrônicos: 1500.0",
        "Vendas em Móveis: 1200.0",
        "Vendas em Alimentos: 340.0",
        "Vendas em Jardinagem: 160.0",
        "Vendas em Livros: 170.0",
        "Vendas em Esportes: 330.0",  
}
