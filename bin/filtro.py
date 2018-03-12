import argparse


def replaceAcuteletters(text):
    text = text.replace('&', '&amp;')
    # Sometimes we really need &, so we escape it!
    listOfReplacements = {'\&amp;': '&',
                          'º': '&ordm;',
                          'ã': '&atilde;',
                          'á': '&aacute;',
                          'é': '&eacute;',
                          'í': '&iacute;',
                          'ó': '&oacute;',
                          'ú': '&uacute;',
                          'Á': '&Aacute;',
                          'á': '&aacute;',
                          'Â': '&Acirc;',
                          'â': '&acirc;',
                          'À': '&Agrave;',
                          'à': '&agrave;',
                          'Ã': '&Atilde;',
                          'ã': '&atilde;',
                          'É': '&Eacute;',
                          'é': '&eacute;',
                          'ê': '&ecirc;',
                          'È': '&Egrave;',
                          'è': '&egrave;',
                          'Ë': '&Euml;',
                          'ë': '&euml;',
                          'Í': '&Iacute;',
                          'í': '&iacute;',
                          'Ó': '&Oacute;',
                          'ó': '&oacute;',
                          'Ô': '&Ocirc;',
                          'ô': '&ocirc;',
                          'Ò': '&Ograve;',
                          'ò': '&ograve;',
                          'Õ': '&Otilde;',
                          'õ': '&otilde;',
                          'Ö': '&Ouml;',
                          'ö': '&ouml;',
                          'Ú': '&Uacute;',
                          'ú': '&uacute;',
                          'Û': '&Ucirc;',
                          'û': '&ucirc;',
                          'Ù': '&Ugrave;',
                          'ù': '&ugrave;',
                          'Ü': '&Uuml;',
                          'ü': '&uuml;',
                          'Ç': '&Ccedil;',
                          'ç': '&ccedil;',
                          'Ñ': '&Ntilde;',
                          'ñ': '&ntilde;',
                          '¿': '&iquest;'}
    for old, new in listOfReplacements.items():
        text = text.replace(old, new)
    return text


def removeHead(text):
    inhead = 0
    i = 0
    while i < len(text):
        if text[i:i+6] == '<head>':
            initialPos = i
            inhead = 1
        elif text[i:i+7] == '</head>' and inhead == 1:
            text = text[:initialPos] + text[(i+7):]
        i += 1
    return text


def removeTableOfContents(text):
    i = 0
    expr = "<h2>Table of Contents</h2>"
    while i < len(text):
        if text[i:i+len(expr)] == expr:
            text = text[:i] + text[(i+len(expr)):]
            return text
        i += 1
    return text


def removeFiUPMfromLinks(text):
    text = text.replace("http://fi.upm.es/", "")
    text = text.replace("https://fi.upm.es/", "")
    return text


def removeTitle(text):
    i = 0
    expr1 = "<h1 class=\"title\">"
    expr2 = "</h1>"
    while i < len(text):
        if text[i:i+len(expr1)] == expr1:
            j = i+len(expr1)
            while j < len(text):
                if text[j:j+len(expr2)] == expr2:
                    text = text[:i] + text[(j+len(expr2)):]
                    return text
                j += 1
        i += 1
    return text


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('file', metavar='file', type=str, nargs='+',
                    help='nombre de la pagina a filtrar')
args = parser.parse_args()

inputFileName = args.file[0]
outputFileName = inputFileName.replace(".html", "-filtered.html")

inputfile = open(inputFileName, 'r')
outputfile = open(outputFileName, 'w')
text = inputfile.read()
inputfile.close()

# Acute letters
text = replaceAcuteletters(text)

# Remove "HEAD"
text = removeHead(text)

# Remove table of contents
text = removeTableOfContents(text)

# Remove unuseful parts of links
text = removeFiUPMfromLinks(text)

text = removeTitle(text)

# print(text)
outputfile.truncate()
outputfile.write(text)
