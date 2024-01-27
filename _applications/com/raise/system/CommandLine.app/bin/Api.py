from bin import Paths
from bin import FinalValue
from bin import Files
import os

class _Ergodic:
    def _Files(__Path:str, __absolutePath:bool=False) -> list:
        __ErgodicResult = []
        if __absolutePath == True:
            for root, dirs, files in os.walk(f"{FinalValue.__ROOTDIR__}/{__Path}", topdown=False):
                __ErgodicResult = Files
        else:
            for root, dirs, files in os.walk(f"{Paths.getSubPaths()}/{__Path}", topdown=False):
                __ErgodicResult = Files
        return __ErgodicResult
    
    def _Dirs(__Path:str, __absolutePath:bool=False) -> list:
        __ErgodicResult = []
        if __absolutePath == True:
            for root, dirs, files in os.walk(f"{FinalValue.__ROOTDIR__}/{__Path}", topdown=False):
                __ErgodicResult = dirs
        else:
            for root, dirs, files in os.walk(f"{Paths.getSubPaths()}/{__Path}", topdown=False):
                __ErgodicResult = dirs
        return __ErgodicResult


def get(__ApplicationName:str, __APIName:str, __Args:list) -> dict:
    """
    Get application API functions, class or variables.
    """
    try:
        __APPPotiner = Files._readfile(f"{FinalValue.__ROOTDIR__}/_registry/applications/point/{__ApplicationName}.item", True)
        __APP = eval(__APPPotiner)["value"]
        __APPAPIS = _Ergodic._Files(f"{__APP}", True)
        if __APPAPIS == [] or __APPAPIS == [""]:
            return {"status":True, "value":""}
        elif __APIName not in __APPAPIS:
            return {"status":False, "value":"NoAPIException"}
        else:
            return {"status":False, "value":Files._readfile(__APP+'/'+__APIName+'.api', True)}
    except SyntaxError:
        return {"status":False, "value":"RegistryItemException"}
    except KeyError:
        return {"status":False, "value":"RegistryItemException"}