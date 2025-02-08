from bisect import bisect_left

class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:

    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """Busca os top_n maiores contratos ainda não renegociados

        Argumentos:
        open_contracts         -- lista com os contratos abertos
        renegotiated_contracts -- lista com os contratos já renegociados
        top_n                  -- máximo tamanho permitido para a resposta

        Nota:
        Não modifica os argumentos, mas cria uma cópia de cada lista. Em seguida
        implementa o seguinte algoritmo com complexidade O(n log n):

        1. Ordena os contratos abertos pelo seus valores em ordem decrescente.
        2. Ordena os ids dos contratos renegociados
        3. Para cada contrato aberto, começando no maior, faz uma busca binária
            pelo seu id dentro dos contratos renegociados
        4. Se o contrato não foi renegociado, adiciona o seu id à lista a ser
            retornada até o máximo tamanho permitido para essa lista
        """
        result = []
        if open_contracts:
            contracts_sorted = sorted(open_contracts, key=lambda x: x.debt, reverse=True)
            renegotiated_sorted = sorted(renegotiated_contracts)

            for c in contracts_sorted:
                if len(result) == top_n:
                    break
                else:
                    is_renegotiated = self._in_sorted(c.id, renegotiated_sorted)

                    if not is_renegotiated:
                        result.append(c.id)

        return result

    def _in_sorted(self, element, sorted_list):
        pos = bisect_left(sorted_list, element)
        result = pos < len(sorted_list) and sorted_list[pos] == element
        return result
