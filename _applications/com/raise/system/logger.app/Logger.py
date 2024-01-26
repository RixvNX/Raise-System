import time
import os
from bin import Paths

__PATH__ = Paths.getSubPaths()
__FileName = str(time.strftime("%Y-%m-%d_%H-%M", time.localtime()))

def log(__from:str, __text:str, __type:str="INFO") -> bool:
    __type = __type.upper()

    LogNameList = []

    for root, dirs, files in os.walk(f"{__PATH__}/logs", topdown=False):
        LogNameList.append(files)

    if f"{__FileName}.log" not in LogNameList:
        CreateLogFile_io = open(f"{__PATH__}/logs/{__FileName}.log", "w+", encoding="utf-8")
        CreateLogFile_io.close()
        
    __IOTmp = open(f"{__PATH__}/logs/{__FileName}.log", "a+", encoding="utf-8")
    __IOTmp.write(f"{time.strftime('[%Y-%m-%d  %H:%M:%S]', time.localtime())} [{__type}] [{__from}] {__text}\n")
    __IOTmp.close()
    return True