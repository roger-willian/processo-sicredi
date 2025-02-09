"""Testes de desempenho da implementação da Questão 2"""

from time import time
from random import choices, shuffle
import os
import pytest
from src.question2 import Orders

class TestPerformanceQuestion2:
    """Testes de desempenho"""

    @pytest.mark.skipif("ENABLE_PERF" not in os.environ, reason="Teste de performance demora muito")
    def test_performance(self):
        """Combinar 1 milhão de requisições não pode levar mais que 10 segundos"""
        n = int(1e6)
        requests = choices(range(10, 101, 10), k=n)
        n_max = 100

        elapsed_time = []
        for i in range(10):
            self.performance_body(requests, n_max, elapsed_time)
            # poderia usar max() fora do loop, mas assim falha mais rápido
            assert elapsed_time[i] < 10

    def performance_body(self, requests, n_max, elapsed_time):
        """Código cujo desempenho interessa"""

        shuffle(requests)
        t = time()
        Orders().combine_orders(requests, n_max)
        elapsed_time.append(time() - t)
