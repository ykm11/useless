from Crypto.PublicKey import RSA

def read_pri(fpem):
    """
        ARGS
            fpem : filename of PEM private

        RETURN
            n, e, d, p, q
    """
    f = open(fpem)
    prikey = RSA.importKey(f.read())

    n = prikey.n
    e = prikey.e
    d = prikey.d
    p = prikey.p
    q = prikey.q

    return n, e, d, p, q

def read_pub(fpem):
    """
        ARGS
            fpem : filename of PEM public

        RETURN
            n, e

    """
    f = open(fpem)
    pubkey = RSA.importKey(f.read())

    n, e = pubkey.n, pubkey.e
    return n, e

def write_pri(n, e, d, fpem="privateKey.pem"):
    """
        ARGS
            n, e, d
            fpem : output file (default is privateKey.pem)

    """
    fout = open(fpem, "wb")
    key = RSA.construct((n,e,d))
    fout.write(key.exportKey())


