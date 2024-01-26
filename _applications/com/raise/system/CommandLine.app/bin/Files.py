from bin import Paths

def _readfile(__fileName:str, __absolutePath:bool=False) -> str:
    try:
        if __absolutePath == False:
            __temp_FileRead = open(f"{Paths.getSubPaths}/{__fileName}")
        else:
            __temp_FileRead = open(__fileName)
        __temp_File = __temp_FileRead.read()
        __temp_FileRead.close()
    except FileNotFoundError:
        return ""
    return str(__temp_File)

def _readfiles(__fileName:str, __absolutePath:bool=False, __ending:bool=False) -> list:
    try:
        if __absolutePath == False:
            __temp_FileRead = open(f"{Paths.getSubPaths}/{__fileName}")
        else:
            __temp_FileRead = open(__fileName)
        __temp_File = __temp_FileRead.readlines()
        __temp_FileRead.close()
        if __ending == False:
            for i in range(0, len(__temp_File)-1):
                __temp_File[i] = __temp_File[i][0:-1:1]
            return __temp_File
        else:
            return __temp_File
    except FileNotFoundError:
        return [""]

def _writefile(__fileName:str, __value:str) -> bool:
    try:
        __temp_FileWrite = open(f"{Paths.getSubPaths}/{__fileName}")
        __temp_FileWrite = __temp_FileWrite.write(str(__value))
        __temp_FileWrite.close()
    except FileNotFoundError:
        return False
    return True