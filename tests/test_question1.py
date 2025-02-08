from src.question1 import Contracts, Contract

class TestQuestion1:

    def test_no_contracts(self):
        """Caso a lista de contratos esteja vazia deve retornar uma lista vazia"""
        contracts = []
        renegotiated = []
        n = 10

        result = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)

        expected = []
        assert result == expected

    def test_single_non_renegotiated(self):
        """Caso apenas um contrato não renegociado, retornar ele"""
        contracts = [Contract(1, 1)]
        renegotiated = []
        n = 10

        result = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)

        expected = [1]
        assert result == expected

    def test_multiple_non_renegotiated(self):
        """Caso todos os contratos não renegociados, retornar no máx. n"""
        contracts = [Contract(x, x) for x in range(100)]
        renegotiated = []
        n = 10

        result = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)

        expected = list(range(n))
        assert result == expected
