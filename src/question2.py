class Orders:
    def combine_orders(self, requests, n_max):
        result = 0
        sorted_requests = sorted(requests)
        while sorted_requests:
            result += 1
            if len(sorted_requests) == 1:
                sorted_requests = []
            elif sorted_requests[0] + sorted_requests[-1] <= n_max:
                sorted_requests = sorted_requests[1:-1]
            else:
                sorted_requests = sorted_requests[1:]

        return result
