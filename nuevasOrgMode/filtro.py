import argparse


def replaceAcuteletters(text):
    text = text.replace('á', '&aacute;')
    text = text.replace('é', '&eacute;')
    text = text.replace('í', '&iacute;')
    text = text.replace('ó', '&oacute;')
    text = text.replace('ú', '&uacute;')
    text = text.replace('ã', '&eacute;')
    # text.replace('Á', '&Aacute;')
    text = text.replace('á', '&aacute;')
    # text.replace('Â', '&Acirc;')
    # text.replace('â', '&acirc;')
    # text.replace('À', '&Agrave;')
    # text.replace('à', '&agrave;')
    # text.replace('Å', '&Aring;')
    # text.replace('å', '&aring;')
    # text.replace('Ã', '&Atilde;')
    # text.replace('ã', '&atilde;')
    # text.replace('Ä', '&Auml;')
    # text.replace('ä', '&auml;')
    # text.replace('Æ', '&AElig;')
    # text.replace('æ', '&aelig;')
    text.replace('É', '&Eacute;')
    text.replace('é', '&eacute;')
    # text.replace('Ê', '&Ecirc;')
    # text.replace('ê', '&ecirc;')
    # text.replace('È', '&Egrave;')
    # text.replace('è', '&egrave;')
    # text.replace('Ë', '&Euml;')
    # text.replace('ë', '&euml;')
    # text.replace('Ð', '&ETH;')
    # text.replace('ð', '&eth;')
    text.replace('Í', '&Iacute;')
    text.replace('í', '&iacute;')
    # text.replace('Î', '&Icirc;')
    # text.replace('î', '&icirc;')
    # text.replace('Ì', '&Igrave;')
    # text.replace('ì', '&igrave;')
    # text.replace('Ï', '&Iuml;')
    # text.replace('ï', '&iuml;')
    text.replace('Ó', '&Oacute;')
    text.replace('ó', '&oacute;')
    # text.replace('Ô', '&Ocirc;')
    # text.replace('ô', '&ocirc;')
    # text.replace('Ò', '&Ograve;')
    # text.replace('ò', '&ograve;')
    # text.replace('Ø', '&Oslash;')
    # text.replace('ø', '&oslash;')
    # text.replace('Õ', '&Otilde;')
    # text.replace('õ', '&otilde;')
    # text.replace('Ö', '&Ouml;')
    # text.replace('ö', '&ouml;')
    text.replace('Ú', '&Uacute;')
    text.replace('ú', '&uacute;')
    # text.replace('Û', '&Ucirc;')
    # text.replace('û', '&ucirc;')
    # text.replace('Ù', '&Ugrave;')
    # text.replace('ù', '&ugrave;')
    # text.replace('Ü', '&Uuml;')
    # text.replace('ü', '&uuml;')
    text.replace('Ç', '&Ccedil;')
    text.replace('ç', '&ccedil;')
    text.replace('Ñ', '&Ntilde;')
    text.replace('ñ', '&ntilde;')
    # text.replace('<', '&lt;')
    # text.replace('>', '&gt;')
    text.replace('&', '&amp;')
    # text.replace('"', '&quot;')
    # text.replace('®', '&reg;')
    # text.replace('©', '&copy;')
    # text.replace('Ý', '&Yacute;')
    # text.replace('ý', '&yacute;')
    # text.replace('Þ', '&THORN;')
    # text.replace('þ', '&thorn;')
    # text.replace('ß', '&szlig;')
    text.replace('¿', '&iquest;')
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
