class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        result = []
        if open_contracts:
            contracts_sorted = sorted(open_contracts, key=lambda x: x.debt, reverse=True)
            non_renegotiated = [x for x in contracts_sorted if x.id not in renegotiated_contracts]
            result = [ x.id for x in non_renegotiated[:top_n] ]

        return result
