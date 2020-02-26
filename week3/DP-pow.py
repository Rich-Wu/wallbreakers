class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {0: 1}
        odds = 0
        toVisit = []
        if n < 0:
            n = -n
            x = 1 / x
        ans = n
        cache[1] = x
        while (n > 1):
            if n % 2 == 1:
                odds += 1
                n -= 1
            if n not in cache:
                toVisit.append(n)
            n /= 2
        for number in reversed(toVisit):
            number = int(number)
            if number / 2 in cache:
                cache[number] = cache[number/2] * cache[number/2]
            else:
                cache[number] = cache[(number/2) - 1] * cache[(number/2) - 1] * cache[2]
        return cache[ans] if ans in cache else cache[ans - 1] * x