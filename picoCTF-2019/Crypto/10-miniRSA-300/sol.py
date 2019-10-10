c = 2205316413931134031074603746928247799030155221252519872649611751702430439402967052009248250289961880642561508086676942304787433622315744241706664042782734376502484888131147533970136649038736862434581066144482993850305122145625013872515429


def find_cubic_root(n):
    a = 1
    b = n

    while b - a > 1:
        mid = (a + b) // 2

        if mid**3 > n:
            b = mid
        else:
            a = mid

    if a ** 3 == n:
        return a
    elif b ** 3 == n:
        return b
    else:
        return 0

p = find_cubic_root(c)

h = str(hex(p)[2:-1]).decode('hex')

print h

#picoCTF{n33d_a_lArg3r_e_21d2334d}