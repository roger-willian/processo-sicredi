from src.question2 import Orders

class TestQuestion2:

    def test_no_orders(self):
        """Sem requisições, sem viagens"""
        orders = []
        n_max = 100

        result = Orders().combine_orders(orders, n_max)

        expected = 0
        assert result == expected