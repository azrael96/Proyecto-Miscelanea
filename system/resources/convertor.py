import os

sizeMEDIUMBLOB = 16777215
sizeBLOB = 65535

def convertToBinaryData(filename):
    try:
        print(os.stat(filename).st_size)
        if os.stat(filename).st_size <= sizeMEDIUMBLOB:
            with open(filename, 'rb') as file:
                binaryData = file.read()
            return binaryData
        else:
            return False
    except:
        print("cerro el Qdialog")