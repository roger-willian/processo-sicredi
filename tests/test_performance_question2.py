from src.question2 import Orders
from time import time
from random import choices, shuffle
import pytest
import os

class TestPerformanceQuestion2:

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
        shuffle(requests)
        t = time()
        result = Orders().combine_orders(requests, n_max)
        elapsed_time.append(time() - t)



