class Orders:
    def combine_orders(self, requests, n_max):
        result = 0
        sorted_requests = sorted(requests, reverse=True)
        start = 0
        end = len(sorted_requests) - 1
        while start <= end:
            result += 1
            if start == end:
                break
            elif sorted_requests[start] + sorted_requests[end] <= n_max:
                start += 1
                end -= 1
            else:
                start += 1

        return result
