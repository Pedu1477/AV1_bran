
class Produto:
    """Representa um produto disponível na loja."""

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_informacoes(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco} | Estoque: {self.estoque} unidades")


class Venda:
    """Representa uma venda, associando um Produto e uma quantidade."""

    def __init__(self, produto_vendido, quantidade):
        self.produto_vendido = produto_vendido 
        self.quantidade = quantidade

    def finalizar_venda(self):
        total = self.quantidade * self.produto_vendido.preco
        print(f"Venda de {self.produto_vendido.nome} finalizada. Total: R$ {total}")


if __name__ == "__main__":
    p1 = Produto("Mouse Gamer", 150.0, 10)
    venda1 = Venda(p1, 2)
    venda1.finalizar_venda()
   