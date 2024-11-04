import os
import mmap
import PyPDF2
import textract
import shutil
import datetime

# IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")

# NAVIGA NEL FILE SYSTEM
for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(sToPrint)

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

def CercaStringaInFileContent(sFile, sString):
    sString = sString.lower()
    iLen = len(sString)
    sOutFileName, sOutFileExt = os.path.splitext(sFile)
    if(sOutFileExt.lower()==".pdf"):
        #print("Riconosciuto file pdf " + sFile)
        return CercaInFilePdf(sFile,sString)
    elif ((sOutFileExt.lower()==".doc") or (sOutFileExt.lower()==".docx")):
        #print("Riconosciuto file doc " + sFile)
        return CercaInFileDoc(sFile,sString)
    #leggiamo il filename
    try:
        with open(sFile) as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            sAppo = s.readline()
            while len(sAppo)> 0 :
                sAppo = sAppo.lower()
                if(sAppo.find(sString.encode())!=-1):
                    return True
                else:
                    sAppo = s.readline()
    except:
        return False

def in_directory(dir1, dir2):
    #make both absolute
    directory1 = os.path.abspath(dir1).lower()
    directory2 = os.path.abspath(dir2).lower()
    print("Dir1: ",directory1)
    print("Dir2: ",directory2)
    if(directory1.find(directory2)!=-1):
        return True
    else:
        return False

def SalvaFile(sFilePath, sFileName, sOutDir):
    os.path.isdir(sFilePath)
    os.makedirs(sOutSubDir, exist_ok=True)
    os.makedirs(sOutDir, exist_ok=True)
    sFilePathNew = sFilePath.replace('_', '__')
    sFilePathNew = sFilePathNew.replace("\\","_")
    sFilePathNew = sFilePathNew.replace("/","_")
    sOutFile = sOutSubDir + "/" + sFilePathNew
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    sOutSubDir = sOutDir + "/" + dt_string
    sOutFile = sOutDir + "/" + sFileName
    print("Devo copiare {0} in {1}".format(sFilePath,sOutFile))
    shutil.copyfile(sFilePath, sOutFile)

for filename in files:
    #print(filename);
    iRet = CercaStringaInFileName(filename,sStringaDaCercare)
    if(iRet == True):
        print("Trovato file: ",filename)
        iNumFileTrovati = iNumFileTrovati + 1
    else:
        pathCompleto = os.path.join(root,filename)
        iRet = CercaStringaInFileContent(pathCompleto ,sStringaDaCercare)