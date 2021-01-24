class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        # need to calculate factors of every ki for pair [ni, ki]
        # then it is a matter of finding number of ways of grouping ki's factors into ni groups
        # to calculate number of factors for each k
        # we use dynammic programming, f(k) = f(k-p) + factor i if p is a prime factor of k
        # we can use Sieve of Eratosthenes which costs nlog(n)log(n) to find prime numbers
        # and for each k, it costs k/log(k) (prime number theorem)
        # finally, given the prime factorization of k = x1^a1*x2^a2...
        # we are actually distributing these prime factors into n buckets, each bucket initially set to be 1
        # for prime factor xi, with occurence of ai, number of ways of distributing xi^ai into n buckets 
        # is nchoosek(n+ai-1, n-1), so the final result is the product of nchoosek(n+ai-1, n-1) for all ai
        from math import factorial, comb
        MOD = 10**9+7
        
        max_k = 0
        for n, k in queries:
            max_k = max(max_k, k)
            
        # Sieve of Ertosthenes to find primes
        is_prime = [True for _ in range(max_k+1)]
        is_prime[0:2] = [False]*2
        for p in range(2, max_k+1):
            if is_prime[p] == True:
                # change all p*k (p*k <= max_k+1) to False
                i = p
                while p*i <= max_k:
                    is_prime[p*i] = False
                    i+=1
        primes = [p for p in range(2, max_k+1) if is_prime[p]]    
        
        # dp
        dp = [None for _ in range(max_k+1)]
        dp[1] = collections.Counter()
        for i in range(2, max_k+1):
            # iterate all primes, if some prime p divides i, then factors of i is factors of i/p + i
            # if i is prime itself, the fomular still holds since factor of 1 is 1
            for p in primes:
                if i%p == 0:
                    dp[i] = dp[i//p] + collections.Counter([p])
                    break
            
        # do queries and find results
        res = []
        for n, k in queries:
            factors = dp[k]
            ans = 1
            for f, c in factors.items():
                ans *= comb(n+c-1, n-1)
            res.append(ans%MOD)
        return res
        