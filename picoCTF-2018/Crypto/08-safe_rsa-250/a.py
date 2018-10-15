def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

ciphertext = 2205316413931134031046440767620541984801091216351222789180535786851451917462804449135087209259828503848304180574549372616172217553002988241140344023060716738565104171296716554122734607654513009667720334889869007276287692856645210293194853
e = 3

plaintext = find_invpow(ciphertext, e)

assert(plaintext**e == ciphertext)

print plaintext
