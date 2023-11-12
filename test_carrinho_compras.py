import pytest

from carrinho import CarrinhoCompras


@pytest.mark.feature('Carrinho de compras')
@pytest.mark.scenario('Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    carrinho = CarrinhoCompras()
    carrinho.adicionar_item('Camiseta', 29.99)
    carrinho.adicionar_item('Calça', 49.99)

    assert carrinho.itens == [
        {'item': 'Camiseta', 'preco': 29.99},
        {'item': 'Calça', 'preco': 49.99},
    ]

    assert carrinho.total() == 79.98


@pytest.mark.feature('Carrinho de compras')
@pytest.mark.scenario('Remover item do carrinho')
def test_remover_item_do_carrinho():
    carrinho = CarrinhoCompras()
    carrinho.adicionar_item('Camiseta', 29.99)
    carrinho.remover_item()

    assert carrinho.itens == []

    assert carrinho.esta_vazio()
