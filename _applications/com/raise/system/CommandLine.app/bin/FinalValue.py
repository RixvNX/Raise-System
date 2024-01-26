from bin import Paths

__ROOTDIRTMP__ = Paths.getPath()
__ROOTDIRTMP__ = __ROOTDIRTMP__.split("/")
__ROOTDIRTMP__.pop(-1)
__ROOTDIRTMP__.pop(-1)
__ROOTDIRTMP__.pop(-1)
__ROOTDIRTMP__.pop(-1)
__ROOTDIR__ = "/".join(__ROOTDIRTMP__)