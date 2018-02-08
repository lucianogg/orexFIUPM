import argparse


def replaceAcuteletters(text):
    text = text.replace('&', '&amp;')
    text = text.replace('º', '&ordm;')
    text = text.replace('ã', '&atilde;')
    text = text.replace('á', '&aacute;')
    text = text.replace('é', '&eacute;')
    text = text.replace('í', '&iacute;')
    text = text.replace('ó', '&oacute;')
    text = text.replace('ú', '&uacute;')
    text = text.replace('Á', '&Aacute;')
    text = text.replace('á', '&aacute;')
    text = text.replace('Â', '&Acirc;')
    text = text.replace('â', '&acirc;')
    text = text.replace('À', '&Agrave;')
    text = text.replace('à', '&agrave;')
    text = text.replace('Ã', '&Atilde;')
    text = text.replace('ã', '&atilde;')
    text = text.replace('É', '&Eacute;')
    text = text.replace('é', '&eacute;')
    text = text.replace('ê', '&ecirc;')
    text = text.replace('È', '&Egrave;')
    text = text.replace('è', '&egrave;')
    text = text.replace('Ë', '&Euml;')
    text = text.replace('ë', '&euml;')
    text = text.replace('Í', '&Iacute;')
    text = text.replace('í', '&iacute;')
    text = text.replace('Ó', '&Oacute;')
    text = text.replace('ó', '&oacute;')
    text = text.replace('Ô', '&Ocirc;')
    text = text.replace('ô', '&ocirc;')
    text = text.replace('Ò', '&Ograve;')
    text = text.replace('ò', '&ograve;')
    text = text.replace('Õ', '&Otilde;')
    text = text.replace('õ', '&otilde;')
    text = text.replace('Ö', '&Ouml;')
    text = text.replace('ö', '&ouml;')
    text = text.replace('Ú', '&Uacute;')
    text = text.replace('ú', '&uacute;')
    text = text.replace('Û', '&Ucirc;')
    text = text.replace('û', '&ucirc;')
    text = text.replace('Ù', '&Ugrave;')
    text = text.replace('ù', '&ugrave;')
    text = text.replace('Ü', '&Uuml;')
    text = text.replace('ü', '&uuml;')
    text = text.replace('Ç', '&Ccedil;')
    text = text.replace('ç', '&ccedil;')
    text = text.replace('Ñ', '&Ntilde;')
    text = text.replace('ñ', '&ntilde;')
    text = text.replace('¿', '&iquest;')
    return text


def removeHead(text):
    inhead = 0
    ititialPos = 0
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

# print(text)
outputfile.truncate()
outputfile.write(text)
