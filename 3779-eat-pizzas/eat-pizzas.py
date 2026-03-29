class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)

        days = n // 4
        odd_days = ceil((n / 4) / 2)
        even_days = days // 2
        l, r = 0, n - 1
        res = 0
        for _ in range(odd_days):
            res += pizzas[r]
            r -= 1
            l += 3
        for _ in range(even_days):
            res += pizzas[r-1]
            r -= 2
            l += 2
        return res