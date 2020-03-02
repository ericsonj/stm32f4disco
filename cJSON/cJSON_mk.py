from pybuild import preutil


def getSrcs(wk):
    return preutil.getAllSrcs_C(wk)


def getIncs(wk):
    return preutil.getAllIncs_C(wk)


def getCompilerOpts(wk):
    opt = wk['compilerOpts']
    opt['CONTROL-C-OPTS'] = ['-std=c89']
    return opt