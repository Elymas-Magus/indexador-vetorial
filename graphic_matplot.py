import matplotlib.pyplot as plt


def make_graph (dic):
    revocacao = list(dic.keys())
    precisao = []
    for elem in dic.keys():
        precisao.append(dic[elem])

    plt.plot(revocacao, precisao)
    plt.show()
        


def maior (dic):
    maior = 0
    for elem in dic:
        if dic[elem] > maior:
            maior = dic[elem]

    return maior

def max (x, dic):
    l = {}
    for elem in l:
        if elem >= x:
            l[elem] = dic[elem]

    m = maior (l)
    return m


def medidor (query, resp):
    count = 0
    dic = {}
    for i in range(len(resp)):
        print(resp, ", ", query)
        if str(resp[i]) in query:
            count += 1
            precisao = (count/(i + 1)) * 100
            revocacao = (count/len(query)) * 100
            dic[revocacao] = precisao

    return dic


def padronizador (dic):
    l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    new_dic = {}
    for elem in l:
        new_dic[elem] = max (elem, dic)

    print(new_dic)
    print(dic)

    return new_dic


def arr (mtz):
    arr = []
    for i in range(len(mtz)):
        arr.append(mtz[i][1])

    return arr


def plotGraphic (queries, mtz):
    for query in queries:        
        dic = medidor(queries[query]["docs"], arr(mtz[query]))
        new_dic = padronizador(dic)
        
        make_graph(new_dic)
        break
