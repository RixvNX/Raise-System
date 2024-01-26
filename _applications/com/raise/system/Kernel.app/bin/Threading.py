"""
Author: RixvNX
Date: 2024/01/26 23:07
"""
import threading

__THREADLOCK__ = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, __threadID:int, __threadName:str, __threadPriority:int=0, __threadStatus="running") -> object:
        super().__init__()
        self.ID = __threadID
        self.name = __threadName
        self.priority = __threadPriority
        self.status = __threadStatus
    
    def run(self) -> None:
        return None

    def acquire(self) -> bool:
        __THREADLOCK__.acquire()
    
    def release(self) -> bool:
        __THREADLOCK__.release()