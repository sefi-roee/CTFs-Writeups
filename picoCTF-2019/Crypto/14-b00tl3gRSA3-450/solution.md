# Problem
Why use p and q when I can use more? Connect with nc 2019shell1.picoctf.com 47259.

## Hints:
There's more prime factors than p and q, finding d is going to be different.

## Solution:

Lets connect:
```bash
nc 2019shell1.picoctf.com 47259

c: 1789478774708178751733610405912626128059579640323419269337009882854177864432649536000996783306574615895842987761671855567950076201359927315161591956190895313706289004928494705344018435608428512660940543070648040835764635047900846125739051779045469953142264047137590080643052730969514531480536665673867755330800111197510364828952629367442928246
n: 2288270088846735357106859785057471410964029178751275985133437188112869387065357149315628435760038495915707758235004078258837389024124261735560004100679591906318506257400142206172954325190681814792847192856119258140772980193363283386441962041988871891225319584672260198913596266911873284127614232167301388894238055511066261585763754427108720961
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

c = 1789478774708178751733610405912626128059579640323419269337009882854177864432649536000996783306574615895842987761671855567950076201359927315161591956190895313706289004928494705344018435608428512660940543070648040835764635047900846125739051779045469953142264047137590080643052730969514531480536665673867755330800111197510364828952629367442928246
n = 2288270088846735357106859785057471410964029178751275985133437188112869387065357149315628435760038495915707758235004078258837389024124261735560004100679591906318506257400142206172954325190681814792847192856119258140772980193363283386441962041988871891225319584672260198913596266911873284127614232167301388894238055511066261585763754427108720961
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
Python 2.7.15 | packaged by conda-forge | (default, Feb 28 2019, 04:00:11) 
Type "copyright", "credits" or "license" for more information.

IPython 5.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:     return True # no base tested showed n as composite
   ...: 
   ...: r = remote('2018shell1.picoctf.com', 11423)
   ...: 
   ...: lines = r.recv().split('\n')
   ...: 
   ...: c = 178947877470817875173361040591262612805957964032341926933700988285417786443264953600099678330657461589584298776167185556795007620135992731516159195619089531370628900492849470534401843560842851
   ...: 2660940543070648040835764635047900846125739051779045469953142264047137590080643052730969514531480536665673867755330800111197510364828952629367442928246
   ...: n = 228827008884673535710685978505747141096402917875127598513343718811286938706535714931562843576003849591570775823500407825883738902412426173556000410067959190631850625740014220617295432519068181
   ...: 4792847192856119258140772980193363283386441962041988871891225319584672260198913596266911873284127614232167301388894238055511066261585763754427108720961
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
   ...:     if not is_probable_prime(factors[0]):
   ...:         f = factors.pop(0)
   ...: 
   ...:         ff = False
   ...:         work = 1000
   ...: 
   ...:         while not ff:
   ...:             ff = lenstra(f, work)
   ...:             work *= 10
   ...: 
   ...:         assert(f % ff == 0)
   ...: 
   ...:         factors.extend([ff, f / ff])
   ...:     else:
   ...:         primes.append(factors.pop(0))
   ...: 
   ...:         log.info('Found prime factor #{} ({})'.format(len(primes), primes[-1]))
   ...: 
   ...: phi = 1
   ...: for p in primes:
   ...:     phi *= (p - 1)
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
[x] Opening connection to 2018shell1.picoctf.com on port 11423: Trying 18.188.70.152
[+] Opening connection to 2018shell1.picoctf.com on port 11423: Done
[*] c: 1789478774708178751733610405912626128059579640323419269337009882854177864432649536000996783306574615895842987761671855567950076201359927315161591956190895313706289004928494705344018435608428512660940543070648040835764635047900846125739051779045469953142264047137590080643052730969514531480536665673867755330800111197510364828952629367442928246
[*] n: 2288270088846735357106859785057471410964029178751275985133437188112869387065357149315628435760038495915707758235004078258837389024124261735560004100679591906318506257400142206172954325190681814792847192856119258140772980193363283386441962041988871891225319584672260198913596266911873284127614232167301388894238055511066261585763754427108720961
[*] e: 65537
[*] Factorizing n (ECM)
[*] Found prime factor #1 (14807385727)
[*] Found prime factor #2 (9197200219)
[*] Found prime factor #3 (9005868947)
[*] Found prime factor #4 (10064895601)
[*] Found prime factor #5 (15732710647)
[*] Found prime factor #6 (9504854237)
[*] Found prime factor #7 (13444434151)
[*] Found prime factor #8 (11818231223)
[*] Found prime factor #9 (9032618123)
[*] Found prime factor #10 (15515699119)
[*] Found prime factor #11 (11197308041)
[*] Found prime factor #12 (9424475771)
[*] Found prime factor #13 (9000257927)
[*] Found prime factor #14 (10639275233)
[*] Found prime factor #15 (15047702401)
[*] Found prime factor #16 (10261669333)
[*] Found prime factor #17 (14949039617)
[*] Found prime factor #18 (12306132463)
[*] Found prime factor #19 (12110007061)
[*] Found prime factor #20 (10721534303)
[*] Found prime factor #21 (10071297889)
[*] Found prime factor #22 (17083009547)
[*] Found prime factor #23 (14437356977)
[*] Found prime factor #24 (13234678063)
[*] Found prime factor #25 (10586550157)
[*] Found prime factor #26 (12928494167)
[*] Found prime factor #27 (11976008657)
[*] Found prime factor #28 (8673621841)
[*] Found prime factor #29 (9820942283)
[*] Found prime factor #30 (12926806967)
[*] Found prime factor #31 (15242750689)
[*] Found prime factor #32 (10810679053)
[*] Found prime factor #33 (16377562727)
[*] Found prime factor #34 (9327627061)
[*] Calculated phi: 2288270082080749725676482769208838739596058422646014091158963311199081673785546172610298252482838643419596067817293121453376724284659464424398055915490701028620560601460252125737169378490240831601693205044244387662885363081529772261603571323816811503693474622290956431861977333312776805245251168455087959715885993653878757473543782400000000000
[*] Calculated d: 879945414172132605802809386294782396437125049476247724573724664980686579226136909564440492532042960334782795995108431067458080251186166935069957507700942175004888357385923586261625382252941841067273023689290737413675281449878897730090379549000278980058332658360570120630873441783246121210778948493295798720718965043640271081194598532810473473
[*] Calculated plaintext: 13016382529449106065933618925167173598170118383294989999418818656303020927826045
[*] In hex: 0x7069636f4354467b746f6f5f6d616e795f666163743072735f333937383933387d
[*] Unhexlified: picoCTF{too_many_fact0rs_3978938}
```

Nice and easy!

Flag: picoCTF{too_many_fact0rs_3978938}
