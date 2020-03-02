from pybuild import preutil


def getSrcs(wk):
    return preutil.getAllSrcs_C(wk)


def getIncs(wk):
    return preutil.getAllIncs_C(wk)


