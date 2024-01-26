from bin import FinalValue
from bin import Files

def get(__ApplicationName:str, __APIName:str, __Args:list):
    __APP = Files._readfile(f"{FinalValue.__ROOTDIR__}/_registry/applications/point/{__ApplicationName}.item", True)