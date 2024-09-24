class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # Multiplica a quantidade pelo valor de cada venda e soma ao total
            total += venda.quantidade * venda.valor
        return total

def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # Exibe o total de vendas usando o método calcular_total_vendas
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total_vendas}")

if __name__ == "__main__":
    main()
