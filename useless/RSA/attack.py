from ..math import extgcd

def common_modulus_attack(c1, c2, e1, e2, n):
    """
        ARGS :
            c1, c2, e1, e2, n

        RETURN :
            m
    """

    g, s, t = extgcd(e1, e2) # s*e1 + t*e2 = g
    assert s*e1 + t*e2 == g

    print(s, t)
    if s < 0:
        s *= -1
        _, c1, _ = extgcd(c1, n)

    if t < 0:
        t *= -1
        _, c2, _ = extgcd(c2, n)

    print(s, t)

    m = pow(c1, s, n) * pow(c2, t, n) % n
    return m
