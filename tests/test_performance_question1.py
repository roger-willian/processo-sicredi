from src.question1 import Contracts, Contract
from time import time
from statistics import mean
import pytest
import os

class TestPerformanceQuestion1:

    @pytest.mark.skipif("ENABLE_PERF" not in os.environ, reason="Teste de performance demora muito")
    def test_performance(self):
        """Retornar 1 milhão de contratos não pode levar mais que 10 segundos"""
        n = int(1e6)
        contracts = [Contract(x, x) for x in range(2*n)]
        renegotiated = list(range(n))

        elapsed_time = []
        for i in range(100):
            self.performance_body(contracts, renegotiated, n, elapsed_time)
            # poderia usar max() fora do loop, mas assim falha mais rápido
            assert elapsed_time[i] < 10

    def performance_body(self, contracts, renegotiated, n, elapsed_time):
        t = time()
        result = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)
        elapsed_time.append(time() - t)



