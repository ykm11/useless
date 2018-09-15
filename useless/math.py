

def gcd(m, n):

    while n > 0:
        m, n = n, m % n
    return m

def extgcd(m, n):
    """
        Extended Euclid
        To find (s, t) satisfying 
            `m*s + n*t == GCD(m, n)`

        RETURN :
            GCD(m, n), s, t

    """
    m0, n0 = m, n

    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while n > 0:
        r = m % n
        q = (m - r) // n
        s1, s0 = s0 - q*s1, s1
        t1, t0 = t0 - q*t1, t1

        m, n = n, m % n

    assert m0*s0 + n0*t0 == m
    return m, s0, t0

def xor(x, y):
    """
        ARGS:
            x [bytes]
            y [bytes]
    """
    assert len(x) != 0 and len(y) != 0
    if len(x) > len(y):
        y = (y*(len(x)//len(y)+1))[:len(x)]
    return bytes([b0 ^ b1 for b0, b1 in zip(x, y)])

def isqrt(n):
    """
        check whether arg_n is square number, or not.

        RETURN :
            if n is sq_num -> sqrt(n)
            otherwise -> -1
    """

    l = 0
    r = n
    while r - l > 1:
        m = (l + r) >> 1
        if m**2 < n:
            l = m
        else:
            r = m
    
    if r**2 == n:
        return r
    else:
        return -1

