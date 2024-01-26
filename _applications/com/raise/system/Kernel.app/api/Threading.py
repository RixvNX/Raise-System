from bin import Threading

class Thread(Threading.Thread):
    def __init__(self, __threadID: int, __threadName: str, __threadPriority: int = 0, __threadStatus="running") -> object:
        super().__init__(__threadID, __threadName, __threadPriority, __threadStatus)

    def run(self) -> None:
        return None
    
    def acquire(self) -> bool:
        return super().acquire()
    
    def release(self) -> bool:
        return super().release()