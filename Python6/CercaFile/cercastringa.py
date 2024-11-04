import PyPDF2
import textract

def CercaStringaInFileName(sFilename, sStringToSearch):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    print("Cerco {0} in {1} ".format(sFilename1,sStringToSearch1))
    iRet = sFilename1.find(sStringToSearch1)
    if(iRet>-1):
        print("Trovato")
        return True
    return False

def CercaInFilePdf(sFile, sString):
    object = PyPDF2.PdfFileReader(sFile)
    numPages = object.getNumPages()
    for i in range(0, numPages):
        pageObj = object.getPage(i)
        text = pageObj.extractText()
        text = text.lower()
        if(text.find(sString)!=-1):
            return True
    return False

def CercaInFileDoc(sFile, sString):
    text = textract.process(sFile)
    text = text.lower()
    if(text.find(sString.encode())!=-1):
        return True
    return False