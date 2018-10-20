# Problem
The more primes, the safer.. right.?.? Connect with ```nc 2018shell1.picoctf.com 11423```.

## Hints:
How would you find d if there are more than 2 prime factors of n?

## Solution:

Lets connect:
```bash
nc 2018shell1.picoctf.com 11423

c: 647973549340428280171651636988671120573017755650712172034796004333270731384682641078277408281800336121596702560365650987987048800349671826117664435204703541305326984653870873388478413192870014024318080150756472386155506317099039867042176940044895978611962688324477355215679355395794401775965369663407852
n: 13428914953707316165921427266228697452858146775685626870931300929100541155134894843920120172990244683944856479121747004610199515948414589194204957094572777299454339465033500525276992471129932727843682899562263499439846215206409434878804696131015780509854954596405105177997599626793428333082199915964575577
e: 65537
```

There are more than two prime factors, maybe we can factorize it...

The code:

[Lenstra.py](https://github.com/delta003/lenstra_algorithm/blob/master/lenstra.py):
```python
import argparse
from random import randint
from fractions import gcd


# Sieve of Eratosthenes
def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in xrange(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in xrange(p, n + 1, p):
                b[i] = False
    return ps


# Finds modular inverse
# Returns inverse, unused helper and gcd
def modular_inv(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = modular_inv(b, r)
    return y, x - q * y, g


# Addition in Elliptic curve modulo m space
def elliptic_add(p, q, a, b, m):
    # If one point is infinity, return other one
    if p[2] == 0: return q
    if q[2] == 0: return p
    if p[0] == q[0]:
        if (p[1] + q[1]) % m == 0:
            return 0, 1, 0  # Infinity
        num = (3 * p[0] * p[0] + a) % m
        denom = (2 * p[1]) % m
    else:
        num = (q[1] - p[1]) % m
        denom = (q[0] - p[0]) % m
    inv, _, g = modular_inv(denom, m)
    # Unable to find inverse, arithmetic breaks
    if g > 1:
        return 0, 0, denom  # Failure
    z = (num * inv * num * inv - p[0] - q[0]) % m
    return z, (num * inv * (p[0] - z) - p[1]) % m, 1


# Multiplication (repeated addition and doubling)
def elliptic_mul(k, p, a, b, m):
    r = (0, 1, 0)  # Infinity
    while k > 0:
        # p is failure, return it
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = elliptic_add(p, r, a, b, m)
        k = k // 2
        p = elliptic_add(p, p, a, b, m)
    return r


# Lenstra's algorithm for factoring
# Limit specifies the amount of work permitted
def lenstra(n, limit):
    g = n
    while g == n:
        # Randomized x and y
        q = randint(0, n - 1), randint(0, n - 1), 1
        # Randomized curve coefficient a, computed b
        a = randint(0, n - 1)
        b = (q[1] * q[1] - q[0] * q[0] * q[0] - a * q[0]) % n
        g = gcd(4 * a * a * a + 27 * b * b, n)  # singularity check
    # If we got lucky, return lucky factor
    if g > 1:
        return g
    # increase k step by step until lcm(1, ..., limit)
    for p in primes(limit):
        pp = p
        while pp < limit:
            q = elliptic_mul(p, q, a, b, n)
            # Elliptic arithmetic breaks
            if q[2] > 1:
                return gcd(q[2], n)
            pp = p * pp
    return False


# Command line tool
def main():
    parser = argparse.ArgumentParser(description = 'Process arguments')
    parser.add_argument('--n', type = int,
                        help = 'number to factor')
    parser.add_argument('--limit', type = int, default = 1000,
                        help = 'work limit (default = 1000)')
    args = parser.parse_args()
    print lenstra(args.n, args.limit)


if __name__ == '__main__':
    main()
```

My script:
```python
#!/usr/bin/env python

from pwn import *
import binascii
from lenstra import lenstra


MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

# From http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
import random

_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
 
    >>> is_probable_prime(1)
    Traceback (most recent call last):
        ...
    AssertionError
    >>> is_probable_prime(2)
    True
    >>> is_probable_prime(3)
    True
    >>> is_probable_prime(4)
    False
    >>> is_probable_prime(5)
    True
    >>> is_probable_prime(123456789)
    False
 
    >>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
    >>> len(primes_under_1000)
    168
    >>> primes_under_1000[-10:]
    [937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
 
    >>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True
 
    >>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    False
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

r = remote('2018shell1.picoctf.com', 11423)

lines = r.recv().split('\n')

c = 647973549340428280171651636988671120573017755650712172034796004333270731384682641078277408281800336121596702560365650987987048800349671826117664435204703541305326984653870873388478413192870014024318080150756472386155506317099039867042176940044895978611962688324477355215679355395794401775965369663407852
n = 13428914953707316165921427266228697452858146775685626870931300929100541155134894843920120172990244683944856479121747004610199515948414589194204957094572777299454339465033500525276992471129932727843682899562263499439846215206409434878804696131015780509854954596405105177997599626793428333082199915964575577
e = 65537

log.info('c: {}'.format(c))
log.info('n: {}'.format(n))
log.info('e: {}'.format(e))

log.info('Factorizing n (ECM)')

factors = [n]
primes = []

while len(factors) > 0:
	if not is_probable_prime(factors[0]):
		f = factors.pop(0)

		ff = False
		work = 1000

		while not ff:
			ff = lenstra(f, work)
			work *= 10

		assert(f % ff == 0)

		factors.extend([ff, f / ff])
	else:
		primes.append(factors.pop(0))

		log.info('Found prime factor #{} ({})'.format(len(primes), primes[-1]))

phi = 1
for p in primes:
	phi *= (p - 1)

log.info('Calculated phi: {}'.format(phi))

d = MMI(e, phi)
log.info('Calculated d: {}'.format(d))

assert((e * d) % phi == 1)

plain = pow(c, d, n)
log.info('Calculated plaintext: {}'.format(plain))
log.info('In hex: {}'.format(hex(plain)))

log.info('Unhexlified: {}'.format(binascii.unhexlify(hex(plain)[2:]))) # python 2
```

The output:
```python
Python 2.7.14 |Anaconda custom (64-bit)| (default, Feb 12 2018, 06:28:32) 
Type "copyright", "credits" or "license" for more information.

IPython 5.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: lines = r.recv().split('\n')
   ...: 
   ...: c = 647973549340428280171651636988671120573017755650712172034796004333270731384682641078277408281800336121596702560365650987987048800349671826117664435204703541305326984653870873388478413192870014
   ...: 024318080150756472386155506317099039867042176940044895978611962688324477355215679355395794401775965369663407852
   ...: n = 134289149537073161659214272662286974528581467756856268709313009291005411551348948439201201729902446839448564791217470046101995159484145891942049570945727772994543394650335005252769924711299327
   ...: 27843682899562263499439846215206409434878804696131015780509854954596405105177997599626793428333082199915964575577
   ...: e = 65537
   ...: 
   ...: log.info('c: {}'.format(c))
   ...: log.info('n: {}'.format(n))
   ...: log.info('e: {}'.format(e))
   ...: 
   ...: log.info('Factorizing n (ECM)')
   ...: 
   ...: factors = [n]
   ...: primes = []
   ...: 
   ...: while len(factors) > 0:
   ...: ^Iif not is_probable_prime(factors[0]):
   ...: ^I^If = factors.pop(0)
   ...: 
   ...: ^I^Iff = False
   ...: ^I^Iwork = 1000
   ...: 
   ...: ^I^Iwhile not ff:
   ...: ^I^I^Iff = lenstra(f, work)
   ...: ^I^I^Iwork *= 10
   ...: 
   ...: ^I^Iassert(f % ff == 0)
   ...: 
   ...: ^I^Ifactors.extend([ff, f / ff])
   ...: ^Ielse:
   ...: ^I^Iprimes.append(factors.pop(0))
   ...: 
   ...: ^I^Ilog.info('Found prime factor #{} ({})'.format(len(primes), primes[-1]))
   ...: 
   ...: phi = 1
   ...: for p in primes:
   ...: ^Iphi *= (p - 1)
   ...: 
   ...: log.info('Calculated phi: {}'.format(phi))
   ...: 
   ...: d = MMI(e, phi)
   ...: log.info('Calculated d: {}'.format(d))
   ...: 
   ...: assert((e * d) % phi == 1)
   ...: 
   ...: plain = pow(c, d, n)
   ...: log.info('Calculated plaintext: {}'.format(plain))
   ...: log.info('In hex: {}'.format(hex(plain)))
   ...: 
   ...: log.info('Unhexlified: {}'.format(binascii.unhexlify(hex(plain)[2:]))) # python 2
   ...: 
[x] Opening connection to 2018shell1.picoctf.com on port 11423
[x] Opening connection to 2018shell1.picoctf.com on port 11423: Trying 18.223.208.176
[+] Opening connection to 2018shell1.picoctf.com on port 11423: Done
[*] c: 647973549340428280171651636988671120573017755650712172034796004333270731384682641078277408281800336121596702560365650987987048800349671826117664435204703541305326984653870873388478413192870014024318080150756472386155506317099039867042176940044895978611962688324477355215679355395794401775965369663407852
[*] n: 13428914953707316165921427266228697452858146775685626870931300929100541155134894843920120172990244683944856479121747004610199515948414589194204957094572777299454339465033500525276992471129932727843682899562263499439846215206409434878804696131015780509854954596405105177997599626793428333082199915964575577
[*] e: 65537
[*] Factorizing n (ECM)
[*] Found prime factor #1 (2664291941)
[*] Found prime factor #2 (3278115143)
[*] Found prime factor #3 (4202662333)
[*] Found prime factor #4 (3939220513)
[*] Found prime factor #5 (4264704553)
[*] Found prime factor #6 (2910076333)
[*] Found prime factor #7 (2944872899)
[*] Found prime factor #8 (2975319937)
[*] Found prime factor #9 (2958852277)
[*] Found prime factor #10 (3501649013)
[*] Found prime factor #11 (3229653593)
[*] Found prime factor #12 (2336198173)
[*] Found prime factor #13 (3408274783)
[*] Found prime factor #14 (3450722783)
[*] Found prime factor #15 (2544331963)
[*] Found prime factor #16 (3555080729)
[*] Found prime factor #17 (3032445743)
[*] Found prime factor #18 (3864798023)
[*] Found prime factor #19 (3012462569)
[*] Found prime factor #20 (3333804337)
[*] Found prime factor #21 (3843212683)
[*] Found prime factor #22 (2322883813)
[*] Found prime factor #23 (2238324797)
[*] Found prime factor #24 (3410137823)
[*] Found prime factor #25 (2724585943)
[*] Found prime factor #26 (4074526433)
[*] Found prime factor #27 (3222570727)
[*] Found prime factor #28 (2751288073)
[*] Found prime factor #29 (2619943093)
[*] Found prime factor #30 (4152153121)
[*] Found prime factor #31 (3252774037)
[*] Found prime factor #32 (3676573787)
[*] Calculated phi: 13428914816946856438723904871649501567081186182239918092952181864144028894557962805010130733155800778328951859681135537037146846105245917848395700795547881238063143458819117037519412438660195449249458182497172168058325489046740408225970619273092402594840378749036704384144607417737465709398714423548313600
[*] Calculated d: 7171704817021529446806180791121542866592024602566445416380462414285686120962642448927393314623083559539089599597780548336056572831890491244546584797048626628197964829923083087617367828144511355779651744623663363932456354679584269769885281208450708619854635644235846215802695570758675249537742112458473473
[*] Calculated plaintext: 13016382529449106065908111207362094589157720258852086801305724876478141755895933
[*] In hex: 0x7069636f4354467b705f265f715f6e305f725f245f7421215f363632393931307d
[*] Unhexlified: picoCTF{p_&_q_n0_r_$_t!!_6629910}
```

Nice and easy!

Flag: picoCTF{p_&_q_n0_r_$_t!!_6629910}
