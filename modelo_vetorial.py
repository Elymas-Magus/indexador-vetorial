import sys
import nltk
import math
import tf_idf
import graphic_matplot as GM
import xml_reader as QR
import xml.etree.ElementTree as ET


def removePonto (string):
    string = string.replace("!", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace(":", "")
    string = string.replace(";", "")
    string = string.replace("?", "")
    string = string.replace("'", "")
    string = string.replace('"', "")
    string = string.replace('`', "")

    return string


def removeSpace (string):
    while (True):
        str_temp = string
        string = string.replace("\n", " ")
        string = string.replace("\r", " ")
        string = string.replace("\t", " ")
        string = string.replace("  ", " ")

        if(str_temp == string):
            break
    
    return string


def setconsulta (consulta, indice, idfs):
    stemmer = nltk.stem.RSLPStemmer()
    stopwords = nltk.corpus.stopwords.words("english")
    consultas = nltk.word_tokenize(consulta.lower())
    
    indice_consulta = {}
    constf_idf = {}
    for item in consultas:
        if item not in stopwords:
            palavra = stemmer.stem(item.strip())
            if palavra in indice:
                if palavra not in indice_consulta:
                    indice_consulta[palavra] = {1 : 1}
                else:
                    indice_consulta[palavra][1] += 1

    constf_idf = tf_idf.ponderador(indice_consulta, 1, idfs)
    
    return constf_idf


def criaIndice (arquivos):
    # dicionario de stopwords
    stopwords = nltk.corpus.stopwords.words("english")
    
    # extrator de radicais
    stemmer = nltk.stem.RSLPStemmer()
    
    indice = {}
    
    # count = numero do arquivo
    # loop para ler o conteudo de cada arquivo
    count = 1
    for arquivo in arquivos:
        if arquivo == "" or len(arquivos) == 0:
            break;
        
        arvore = ET.parse(arquivo)
        document = arvore.getroot()

        conteudo = QR.listaSubElementos(document, "")
        conteudo = removePonto(removeSpace(conteudo))
        palavras = nltk.word_tokenize(conteudo.lower())

        for p in palavras:
            palavra = stemmer.stem(p)
            if p not in stopwords:
                if palavra not in indice:
                    indice[palavra] = {count: 1}
                        
                else:
                    if count in indice[palavra]:
                        indice[palavra][count] += 1
                        
                    if count not in indice[palavra]:
                        indice[palavra][count] = 1
   
        count += 1

        
    # cria/abre o arquivo indice
    arq_indice = open("indice.txt", "w")

    for i in indice:
        txt = i + ". " + str(indice[i]) + "\n"
        txt = txt.replace(": ", ",").replace(", ", " ").replace(". ", ": ")
        txt = txt.replace("{", "").replace("}", "")
        arq_indice.write(txt)

    arq_indice.close()

        
    return indice


def main ():
    indice = {}

    # recebe o nome do arquivo base
    entrada = sys.argv

    # abre o arquivo base
    base = open("base.txt", 'r')

    # le e separa os nomes dos arquivos da base
    # cria um lista com os nomes
    arquivos = base.read().strip().split('\n')

    indice = criaIndice(arquivos)

    idfs = {}
    for palavra in indice:
        idfs[palavra] = tf_idf.idf (len(arquivos), len(indice[palavra]))
        
    pesos = tf_idf.ponderador (indice, len(arquivos), idfs)
    
    # cria/abre o arquivo de pesos
    arq_peso = open("pesos.txt", "w")
    for peso in pesos:
        txt = arquivos[peso - 1] + ":"
        for palavra in pesos[peso]:
            if pesos[peso][palavra] != 0:
                txt += "  " + palavra + "," + str(pesos[peso][palavra])
        
        arq_peso.write(txt + "\n")

    arq_peso.close()
        
    
    # abre o arquivo de consultas
    cc = ET.parse("queries.txt")
    consultas = cc.getroot()
    queries = QR.find_queries(consultas)
    
    cons_tfidf = {}
    for query in queries:
        temp = queries[query]["text"]
        cons_tfidf[query] = setconsulta(removePonto(removeSpace(temp)), indice, idfs)

    print("stop1")
    mtz = {}
    for query in queries:
        dic_cos = {}
        for peso in pesos:
            aux = tf_idf.cos(pesos[peso], cons_tfidf[query][1])
            if aux > 0.05:
                dic_cos[peso] = aux
            
        i = 0
        list_cos = [0] * len(dic_cos)
        for cos in dic_cos:
            list_cos[i] = [None, None]
            list_cos[i][0] = dic_cos[cos]
            list_cos[i][1] = cos
            i += 1

        array_cos = [0] * len(list_cos)
        list_cos.sort(reverse = True)
        ''' for i in range(len(list_cos)):
            array_cos[i] = list_cos[i][1]'''
            
        mtz[query] = list_cos

    print("stop2")

    GM.plotGraphic (queries, mtz)
    
    base.close()

main()
