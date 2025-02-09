class Orders:
    def combine_orders(self, requests, n_max):
        result = 0
        if requests:
            if sum(requests) <= n_max:
                result = 1
            else:
                result = len(requests)

        return result
