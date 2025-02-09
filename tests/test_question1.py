"""Testes unitários da implementação da Questão 1"""

from src.question1 import Contracts, Contract

class TestQuestion1:
    """Classe com os testes unitários"""

    def test_no_contracts(self):
        """Caso a lista de contratos esteja vazia deve retornar uma lista vazia"""
        contracts = []
        renegotiated = []
        n = 10

        result = Contracts().get_top_n_open_contracts(contracts, renegotiated, n)

        expected = []
        assert result == expected

    def test_single_non_renegotiated(self):
        """Caso apenas um contrato não renegociado, retornar ele"""
        contracts = [Contract(1, 1)]
        renegotiated = []
        n = 10

        result = Contracts().get_top_n_open_contracts(contracts, renegotiated, n)

        expected = [1]
        assert result == expected

    def test_multiple_non_renegotiated(self):
        """Caso todos os contratos não renegociados, retornar no máx. os n maiores"""
        contracts = [Contract(x, x) for x in range(100)]
        renegotiated = []
        n = 10

        result = Contracts().get_top_n_open_contracts(contracts, renegotiated, n)

        expected = [x.id_ for x in contracts[-n:]]
        expected.reverse()
        assert result == expected

    def test_multiple_but_one_renegotiated(self):
        """Caso um dos maiores contratos foi renegociado, não retorná-lo"""
        contracts = [Contract(x, x) for x in range(1,6)]
        renegotiated = [3]
        n = 3

        result = Contracts().get_top_n_open_contracts(contracts, renegotiated, n)

        expected = [5, 4, 2]
        assert result == expected
