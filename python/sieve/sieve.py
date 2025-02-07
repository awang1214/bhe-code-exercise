import math

"""

Resources used: https://stackoverflow.com/questions/1042717/is-there-a-way-to-find-the-approximate-value-of-the-nth-prime/1069023#1069023
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

"""

class Sieve:
    def __init__(self) -> None:
        pass

    def nth_prime(self, n: int) -> int:
        """
        Find nth prime number given n using Prime number theorem and Sieve of Eratosthenes
        Upped bound logic:
        - n <= 6: 15
        - 6 < n < 7022: n * (log(n) + log(log(n)))
        - 7022 <= n: n * (log(n) + log(log(n)) - 0.9385)
        """
        if n <= 6:
            upper_bound = 15
        elif n < 7022:
            upper_bound = int(n * (math.log(n) + math.log(math.log(n))))
        else:
            upper_bound = int(n * (math.log(n) + math.log(math.log(n)) - 0.9385))

        sieve = [True] * (upper_bound + 1)
        sieve[0] = sieve[1] = False

        for num in range(2, int(math.sqrt(upper_bound)) + 1):
            if sieve[num]:
                for multiple in range(num * num, upper_bound + 1, num):
                    sieve[multiple] = False

        primes = [i for i, is_prime in enumerate(sieve) if is_prime]

        return primes[n]