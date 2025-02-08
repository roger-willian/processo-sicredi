from src.question1 import Contracts

class TestQuestion1:

    def test_no_contracts(self):
        """Caso a lista de contratos esteja vazia deve retornar uma lista vazia"""
        contracts = []
        renegotiated = []
        n = 10

        result = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)

        expected = []
        assert result == expected