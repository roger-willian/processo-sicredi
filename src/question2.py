"""Questão 2 - requisições de transporte de valores monetários"""

# pylint: disable=R0903
class Orders:
    """Trata requisições de transporte de valores monetários"""

    def combine_orders(self, requests, n_max):
        """Combina requisições de transporte de valores monetários.

        Combina no máximo duas a duas, desde que não ultrapasse o valor limite.

        Argumentos:
        requests -- a lista de valores monetários a serem transportados.
        n_max    -- valor máximo combinado permitido.

        Retorna: a quantidade mínima de viagens para transportar todos os valores.
        """

        result = 0
        sorted_requests = sorted(requests, reverse=True)
        start = 0
        end = len(sorted_requests) - 1
        while start <= end:
            result += 1
            if start == end:
                break

            if sorted_requests[start] + sorted_requests[end] <= n_max:
                start += 1
                end -= 1
            else:
                start += 1

        return result
