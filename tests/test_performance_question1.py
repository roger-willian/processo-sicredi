"""Testes de desempenho da implementação da Questão 1"""

from time import time
from random import shuffle
import os
import pytest
from src.question1 import Contracts, Contract

class TestPerformanceQuestion1:
    """Classe com os testes de desempenho"""

    @pytest.mark.skipif("ENABLE_PERF" not in os.environ, reason="Teste de performance demora muito")
    def test_performance(self):
        """Retornar 1 milhão de contratos não pode levar mais que 10 segundos"""

        n = int(1e6)
        contracts = [Contract(x, x) for x in range(2*n)]
        renegotiated = list(range(n))

        elapsed_time = []
        for i in range(10):
            self.performance_body(contracts, renegotiated, n, elapsed_time)
            # poderia usar max() fora do loop, mas assim falha mais rápido
            assert elapsed_time[i] < 10

    def performance_body(self, contracts, renegotiated, n, elapsed_time):
        """Código cujo desempenho interessa"""

        shuffle(contracts)
        shuffle(renegotiated)
        t = time()
        Contracts().get_top_n_open_contracts(contracts, renegotiated, n)
        elapsed_time.append(time() - t)
