
# Topologia estrella

def star(zA, zB, zC, VAN, VBN, VCN):
    VnN = ((1 / zA) * VAN + (1 / zB) * VBN + (1 / zC) * VCN) / ((1 / zA) + (1 / zB) + (1 / zC))

    Van = VAN - VnN
    Vbn = VBN - VnN
    Vcn = VCN - VnN

    Ia = Van / zA
    Ib = Vbn / zB
    Ic = Vcn / zC

    In = Ia + Ib + Ic

    return VnN, Van, Vbn, Vcn, Ia, Ib, Ic, In

def delta(zA, zB, zC, VAN, VBN, VCN):
    Vab = VAN - VBN
    Vbc = VBN - VCN
    Vca = VCN - VAN

    VnN = 0

    Iab = Vab / zA
    Ibc = Vbc / zB
    Ica = Vca / zC

    Ia = Iab - Ica
    Ib = Ibc - Iab
    Ic = Ica - Ibc

    return VnN, Vab, Vbc, Vca, Iab, Ibc, Ica

def star_grounded(zA, zB, zC, VAN, VBN, VCN):
    VnN = 0

    Van = VAN - VnN
    Vbn = VBN - VnN
    Vcn = VCN - VnN


    Ia = Van / zA
    Ib = Vbn / zB
    Ic = Vcn / zC

    In = Ia + Ib + Ic

    return VnN, Van, Vbn, Vcn, Ia, Ib, Ic, In
