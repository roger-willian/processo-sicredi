class Orders:
    def combine_orders(self, requests, n_max):
        result = 0
        if requests:
            sorted_requests = sorted(requests)
            if len(sorted_requests) == 1:
                result = 1
            elif sorted_requests[0] + sorted_requests[-1] <= n_max:
                result = 1 + self.combine_orders(sorted_requests[1:-1], n_max)
            else:
                result = 1 + self.combine_orders(sorted_requests[1:], n_max)

        return result
