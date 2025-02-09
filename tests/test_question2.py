from src.question2 import Orders

class TestQuestion2:

    def test_no_orders(self):
        """Sem requisições, sem viagens"""
        orders = []
        n_max = 100

        result = Orders().combine_orders(orders, n_max)

        expected = 0
        assert result == expected

    def test_single_order(self):
        """Uma única requisição, uma única viagem"""
        orders = [50]
        n_max = 100

        result = Orders().combine_orders(orders, n_max)

        expected = 1
        assert result == expected

    def test_two_orders_not_combinable(self):
        """Duas requisições não combináveis, duas viagens"""
        orders = [60, 60]
        n_max = 100

        result = Orders().combine_orders(orders, n_max)

        expected = 2
        assert result == expected

    def test_two_orders_combinable(self):
        """Duas requisições combináveis, apenas uma viagem"""
        orders = [40, 40]
        n_max = 100

        result = Orders().combine_orders(orders, n_max)

        expected = 1
        assert result == expected