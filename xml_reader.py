import xml.etree.ElementTree as ET

def find_queries(allquerys):
    dic = {}
    num = 0

    reldoc = {}
    for querys in allquerys:
        name = ""
        numdocs = 0
        for elemento in querys:
            if elemento.tag == "number":
                num = elemento.text
                dic[elemento.text] = {None, None, None}
                
            if elemento.tag == "text":
                name = elemento.text

            if elemento.tag == "numberofrelevantdocs":
                numdocs = elemento.text
                docnum = 0
                alldocs = [docnum] * int(numdocs)

            if elemento.tag == "relevantdoc":
                for info_doc in elemento:
                    if info_doc.tag == "docnumber":
                        alldocs[docnum] = info_doc.text
                        docnum += 1

        dic[num] = {"text": name, "numdocs": numdocs, "docs": alldocs}


    return dic

        
def listaSubElementos(document, txt):
    for elem in document:
        if elem.text != "" or elem.text != " " or elem.text != " ":
            txt += elem.text

        if len(elem) > 0:
            txt = listaSubElementos(elem, txt)

    return txt

