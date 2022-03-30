import math

def idf (tam, n):
    idf_ki = math.log10(tam/n)
    return idf_ki


def tf (freq):
    tf_ij = 1 + math.log10(freq)
    return tf_ij


def ponderador (indice, qnt_arquivos, idfs):
    tf_idf = {}
    for i in range(1,qnt_arquivos+1):
        temp = {}
        for palavra in indice:
            if i in indice[palavra]:
                temp[palavra] = tf (indice[palavra][i]) * idfs[palavra]

        tf_idf[i] = temp

    return tf_idf


def prod_interno (u, v):
    prod = 0
    for chave in u.keys():
        if chave in v:
            prod += u[chave] * v[chave]
        
    return prod


def norma(v):
    tam = 0
    for elem in v:
        tam += v[elem]**2
        
    tam = math.sqrt(tam)
    return tam


def cos (u, v):
    if norma(u) == 0:
        print("u")
    if norma(v) == 0:
        print("v")

    cos_theta = prod_interno (u, v)/(norma(u) * norma(v))
    return cos_theta

