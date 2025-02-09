class Orders:
    def combine_orders(self, requests, n_max):
        result = 0
        if requests:
            sorted_requests = sorted(requests)
            result = self._combine_orders_recursive(sorted_requests, n_max, 0)

        return result

    def _combine_orders_recursive(self, requests, n_max, result):
        if not requests:
            return result
        elif len(requests) == 1:
            return 1 + result
        elif requests[0] + requests[-1] <= n_max:
            return self._combine_orders_recursive(requests[1:-1], n_max, 1 + result)
        else:
            return self._combine_orders_recursive(requests[1:], n_max, 1 + result)
